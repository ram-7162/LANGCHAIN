from langchain_core.prompts import ChatPromptTemplate
# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


#  ###  wrong method :- illogical behaviour
# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are an helpful {domain} expert"),
#     HumanMessage(content = "Explain in simple terms, what is {topic}")
# ])

# prompt = chat_template.invoke({
#     "domain " : "cricket ",
#     "topic" : "dusra"
# })

# print(prompt)







chat_template = ChatPromptTemplate([
    ('system', "You are an helpful {domain} expert"),
    ('human', "Explain in simple terms, what is {topic}")
])


### It is the idiomatic and recommended approach in the documentation.
chat_template2 = ChatPromptTemplate.from_messages([
    ('system', "You are an helpful {domain} expert"),
    ('human', "Explain in simple terms, what is {topic}")
])


prompt = chat_template.invoke({
    "domain" : "cricket ",
    "topic" : "dusra"
})

prompt2 = chat_template2.invoke({
    "domain" : "AI ",
    "topic" : "llm"
})

print(prompt.messages)  ### output -> [SystemMessage(content='You are an helpful cricket  expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is dusra', additional_kwargs={}, response_metadata={})]

print(prompt2.messages)  ### output -> [SystemMessage(content='You are an helpful AI  expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is llm', additional_kwargs={}, response_metadata={})]






