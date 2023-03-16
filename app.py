from fastapi import FastAPI
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain

app = FastAPI()

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = Cohere(cohere_api_key="chq8TigoO444FeAiqHOHWfHSXfjAbzyggVImW5jx")

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

response = llm_chain.run(question)

@app.get("/")
def main():
    return {"message": response}
