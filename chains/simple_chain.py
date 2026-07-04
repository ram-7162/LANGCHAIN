from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
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

prompt = PromptTemplate(
    template="Write a 5 line about {topic}",
    input_variables=["topic"]

)

chain = prompt | chat_model | parser

result = chain.invoke({"topic" : "kabaddi"})
print(result)