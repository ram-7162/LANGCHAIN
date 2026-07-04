from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from typing import Annotated, Optional, Literal
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
load_dotenv()

# llm = HuggingFacePipeline.from_model_id(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     pipeline_kwargs={
#         "temperature": 0.5,
#         "max_new_tokens": 200
#     }
# )

# chat_model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name : str = Field(description="Name of the person"),
    age : int = Field(description="Age of the person"),
    city : str = Field(description="name of the city from where person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template="Generate the name, age & city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)
prompt = template.invoke({"place" : "jaipur"})

print(prompt)
# result = chat_model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)














# ##parser.get_format_instructions() does not parse anything.
# ##It only adds instructions to the prompt like:

# ##"Return output in JSON with fields name, age, city"

# ##So the flow is:

# ##Person class → tells parser what structure you want
# ##parser.get_format_instructions() → converts that structure into text instructions for the LLM
# ##LLM generates text
# ##parser.parse(result.content) → takes that text and converts it into a real Person object
