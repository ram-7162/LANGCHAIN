from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200
    }
)

chat_model = ChatHuggingFace(llm=llm)

# 1st -> template :- detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variable = ["topic"]
)


#2nd prompt :- summary

template2 = PromptTemplate(
    template="Write a 5 line summary on {text}",
    input_variables=["text"]
)




# prompt1 = template1.invoke({'topic' : 'black body'})

# result = chat_model.invoke(prompt1)

# prompt2 = template2.invoke({'text' : result.content})

# result1 = model.invoke(prompt2)

# print(result1.content)






parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : "black hole"})