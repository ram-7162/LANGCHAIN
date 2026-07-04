# from langchain_huggingface import HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
#     task="text-generation"
# )

# print(llm.invoke("What is the capital of India?"))




from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
load_dotenv()

llm_endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="conversational",
    huggingfacehub_api_token=os.environ["HF_API_KEY_CONV"]
)

chat_model = ChatHuggingFace(llm=llm_endpoint)

print(chat_model.invoke("What is the capital of India?").content)




