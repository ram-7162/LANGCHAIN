from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace



llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200
    }
)



messages = [
    SystemMessage(content="You are an helpful ai assistant."),
    HumanMessage(content = "Tell me about langchain")
]


hat_model = ChatHuggingFace(llm=llm)



result = chat_model.invoke(messages)
messages.append(AIMessage(content=result.content))


print(messages)

