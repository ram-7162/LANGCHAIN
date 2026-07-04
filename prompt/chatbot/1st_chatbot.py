from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200
    }
)

chat_model = ChatHuggingFace(llm=llm)







# chat_history = []
# while True:
#     user_input = input("You : ")
#     chat_history.append(user_input)
#     if user_input.lower() == "exit":
#         break
#     else:
#         result = chat_model.invoke(chat_history)
#         chat_history.append(result.content)
#         print("AI : ", result.content)



















chat_history = [
    SystemMessage(content = "You are an helpful ai assisant.")
]
while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input.lower() == "exit":
        break
    else:
        result = chat_model.invoke(chat_history)
        chat_history.append(AIMessage(content = result.content))
        print("AI : ", result.content)
