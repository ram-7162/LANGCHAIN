from langchain_community.document_loaders import WebBaseLoader

url = r"https://www.lenovo.com/in/en/p/laptops/ideapad/ideapad-s-series/lenovo-ideapad-slim-5-gen-10-14-inch-amd/83hx001nin?orgRef=https%253A%252F%252Fwww.google.com%252F&srsltid=AfmBOopphdGOQpSfnGN-GAL82nCY6HSPVJfoViyXREp3_7PuuKw_MXea"
loader = WebBaseLoader(url)

docs = loader.load()

print(type(docs))