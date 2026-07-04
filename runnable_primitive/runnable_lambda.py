from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


######-------------------------------------
# def wordCounter(text):
#     return len(text.split())

# runnable_word_counter = RunnableLambda(wordCounter)

# result = runnable_word_counter.invoke("Hey, my name is rohit")
# print(result)
####----------------------------------------


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200
    }
)

chat_model = ChatHuggingFace(llm=llm)

def wordCounter(text):
    return len(text.split())


parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)
joke_gen_chain = RunnableSequence(prompt , chat_model , parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(wordCounter)
})

final_chain = joke_gen_chain | parallel_chain
result = final_chain.invoke({'topic' : 'Ai'})

final_result = f"{result['joke']} \n word count - {result['word_count']}"
