from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = r"C:\Users\Rahul\OneDrive\Desktop\Documents",
    glob = "*.pdf",
    loader_cls=PyPDFLoader
)

# docs = loader.load()

# # print(len(docs))

# for document in docs:
#     print(document.metadata)



docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
