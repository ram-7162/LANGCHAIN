from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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
    template="Write a detailed report about {topic}",
    input_variables = ['topic']
)

Prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = Prompt1 | chat_model | parser

cond_chain = RunnableBranch(
    (lambda x : len(x.split())>500, RunnableSequence(Prompt2 | chat_model | parser)),
    RunnablePassthrough()
)

final_chain = report_gen_chain | cond_chain

result = final_chain.invoke({'topic' : "AI"})

print(result)


