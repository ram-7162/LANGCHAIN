from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
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
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a random person. \n {format_instruction}",
    input_variables= [],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)
#  ######## here format instruction is for knowing type of file(like json)
prompt = template.format()
print(prompt)
# result = chat_model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# print(type(final_result))









 ######## here format instruction is for knowing type of file(like json)
# chain = template | chat_model | parser
# result = chain.invoke({})
# print(result)

