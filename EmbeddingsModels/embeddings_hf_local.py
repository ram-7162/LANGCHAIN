# from langchain_huggingface import HuggingFaceEmbeddings

# embeddding = HuggingFaceEmbeddings(
#     model_name  = "sentence-transformers/all-MiniLM-L6-v2"
# )
# text = "What is capital of INDIA?"

# vector = embeddding.embed_query(text)

# print(type(vector))
# print(str(vector))















from langchain_huggingface import HuggingFaceEmbeddings

embeddding = HuggingFaceEmbeddings(
    model_name  = "sentence-transformers/all-MiniLM-L6-v2"
)
documents = {
    "India is GOAT",
    "Myself rohit jhajhra",
    "I live in India ",
    "I studied from saint lawrence public school",
    "lapalace correction factor"
}
vector = embeddding.embed_documents(documents)

print(type(vector))
print(str(vector))