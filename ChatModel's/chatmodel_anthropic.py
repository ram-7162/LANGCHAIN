from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

anthropic = ChatAnthropic(model = "Claude Opus 4.5")

result = anthropic.invoke("Who is goat of cricket?")

print(result)