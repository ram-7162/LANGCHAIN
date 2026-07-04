from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from typing import Annotated, Optional, Literal
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableSequence
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

prompt = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following joke - {text}",
    input_variables = ['text']
)
parser = StrOutputParser()

chain = RunnableSequence(prompt, chat_model, parser, prompt2, chat_model, parser)
print(chain.invoke({'topic' : 'AI'}))