from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel


load_dotenv()


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 200
    }
)
chat_model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a small paragragh from given \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Make five question & answers from given \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the given paragraph and quiz into a single document \n notes -> {notes} && quiz -> {quiz}",
    input_variables=['notes', 'quiz']
)

parallel_chain = RunnableParallel({
    "notes": prompt1 | chat_model | parser,
    "quiz": prompt2 | chat_model | parser,
})
####Both branches receive the same input.

merge_chain = prompt3 | chat_model | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'text' : """
                                   Established in 2009, the Indian Institute of Technology Indore (IIT Indore) is a premier "second-generation" IIT that has rapidly distinguished itself through a heavy emphasis on high-impact research and global academic standards. Located on a sprawling 501-acre permanent campus in Simrol, about 25 km from the city center, the institute is consistently ranked among the top engineering schools in India, securing the #12 spot in the 2025 NIRF Engineering rankings. IIT Indore is particularly known for its state-of-the-art Sophisticated Instrumentation Centre (SIC), which serves as a national facility housing advanced analytical tools like NMR and Mass Spectrometry, reflecting its commitment to interdisciplinary science.

Beyond academics, the campus offers a vibrant lifestyle with modern 5-BHK hostel units where each student has their own bedroom, a unique feature among IITs. The institute's annual techno-cultural festival, Fluxus, is the largest of its kind in Central India, drawing thousands of participants. With a strong focus on "learning by doing," the curriculum offers diverse programs including B.Tech, M.Tech, and specialized courses like Space Science and Engineering. Its placement records remain stellar, with 2026 reports indicating average packages for Computer Science reaching approximately ₹28.5 LPA, cementing its status as a top-tier destination for aspiring engineers and researchers. """})


print(result)