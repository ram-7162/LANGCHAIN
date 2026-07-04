from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200
    }
)
chat_model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description="Give the sentiment of feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template=(
        "Classify sentiment as positive or negative.\n"
        "Respond ONLY as JSON:\n"
        '{{"sentiment": "positive"}}\n\n'
        "Feedback: {feedback}"
    ),
    input_variables=["feedback"],
)


classifier_chain = prompt1 | chat_model | parser2

# feedback = classifier_chain.invoke({'feedback' : "This is a terrible phone"}).sentiment
####The output of classifier_chain is not just a string; it is a Python Object that has an attribute named sentiment.
###the output looks like --->> sentiment : "positive"
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables = ['feedback']
)


prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables = ['feedback']
)



branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | chat_model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | chat_model | parser),
    RunnableLambda(lambda x : "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback' : "This is a wonderful phone"})
print(result)
print("\n\n\n\n")

chain.get_graph().print_ascii()