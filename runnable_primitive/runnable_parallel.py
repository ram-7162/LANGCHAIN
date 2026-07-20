from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200
    }
)

chat_model = ChatHuggingFace(llm=llm)

Prompt1 = PromptTemplate(
    template = "Write a post for X on {topic}",
    input_variables=['topic']
)

Prompt2 = PromptTemplate(
    template = "Write a post for linkedin on {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'tweet' : Prompt1 | chat_model|parser,
    'linkedin' : Prompt2 | chat_model | parser
}
)

#### Both branches receive the same input.

result = parallel_chain.invoke({'topic' : 'India'})
########## result is dictionary with two topic as key
print(result)

##EXPECTED OUTPUT
## {
#   "tweet": "Some short, catchy post about India (tweet-style)",
#   "linkedin": "A more professional, longer post about India (LinkedIn-style)"
# }