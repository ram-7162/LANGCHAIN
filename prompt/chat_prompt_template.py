from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
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



prompt = chat_template.invoke({
    "domain" : "cricket ",
    "topic" : "dusra"
})

print(prompt)



