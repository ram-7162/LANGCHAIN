from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def documents_embeddings():
    documents = [
        "Sachin Tendulkar is known as the God of Cricket for his unmatched consistency.",
        "Virat Kohli is a modern batting great with aggressive leadership.",
        "MS Dhoni is famous for his calm captaincy and finishing skills.",
        "Rohit Sharma is admired for his elegant batting and big hundreds.",
        "Jasprit Bumrah is a lethal fast bowler with a unique action."
    ]
    embeddings = embedding.embed_documents(documents)
    return np.array(embeddings)

def query_embedding(query):
    embedding_query = embedding.embed_query(query)
    return np.array(embedding_query)

query = "tell me about virat kohli"

doc_embeds = documents_embeddings()
query_embed = query_embedding(query)



#// cosine similarity requires 2D list/array
similarities = cosine_similarity([query_embed], doc_embeds)
print(similarities)
