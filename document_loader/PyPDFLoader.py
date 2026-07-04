from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\Rahul\OneDrive\Desktop\langchain\content.txt")

doc = loader.load()

print(len(doc))
print(doc)