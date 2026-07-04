from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough




### ----------------------------------------------------------------------------------------
# passthrough = RunnablePassthrough()
# result = passthrough.invoke({'name' : "rohit"})
# print(result)

### --------------------------------------------------------------------
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

joke_gen_chain = RunnableSequence(Prompt1, chat_model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : Prompt2 | chat_model | parser 
})

final_chain = joke_gen_chain | parallel_chain

result = final_chain.invoke({'topic' : 'AI'})