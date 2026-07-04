from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\Rahul\OneDrive\Desktop\langchain\cricket.txt", "utf-8")

result = loader.load()
print(type(result))
print(result)
print(result[0])
print(result[0].metadata)
print(result[0].page_content)