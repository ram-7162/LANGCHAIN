from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0
)

result = llm.invoke("What is the capital of India?")
print(result.content)










# from google.genai import Client
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Initialize the client
# client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

# # Create a chat session 
# # (gemini-2.0-flash is usually the best balance of speed and smarts)
# chat = client.chats.create(model="gemini-1.5-flash")

# print("--- Gemini Chat Active (Type 'exit' to stop) ---")

# while True:
#     user_input = input("You: ")
    
#     if user_input.lower() in ['exit', 'quit', 'bye']:
#         print("Gemini: Goodbye!")
#         break

#     try:
#         # Send message and get the response
#         response = chat.send_message(user_input)
#         print(f"Gemini: {response.text}")
#         print("-" * 30)
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
