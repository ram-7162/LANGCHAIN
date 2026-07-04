from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(r"notes.csv")

docs = loader.load()

print(type(docs))