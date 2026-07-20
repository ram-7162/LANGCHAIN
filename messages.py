from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
# from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()


llm3 = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.environ['GROQ_API_KEY4']
    # other params...
)

# llm = HuggingFacePipeline.from_model_id(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     pipeline_kwargs={
#         "temperature": 0.5,
#         "max_new_tokens": 200
#     }
# )



messages = [
    SystemMessage(content="You are an helpful ai assistant."),
    HumanMessage(content = "Tell me about langchain")
]


# hat_model = ChatHuggingFace(llm=llm)

chat_model = llm3

result = chat_model.invoke(messages)
messages.append(AIMessage(content=result.content))

 
print(messages)

