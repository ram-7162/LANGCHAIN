from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    dimensions=32,
)


documents = {
    "India is GOAT",
    "Myself rohit jhajhra",
    "I live in India ",
    "I studied from saint lawrence public school",
    "lapalace correction factor"
}
result = embeddings.embed_documents(documents)
print(result)