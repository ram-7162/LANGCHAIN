# from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()

template = PromptTemplate(
    template = 'Greet this person in 5 languages. The name of the person is {name}',
    input_variables = ['name']
)

prompt1 = template.format(**{'name' : 'nitish'})
prompt2 = template.invoke({'name':'nitish'})
print(prompt1)
print(prompt2)

# result = model.invoke(prompt2)
