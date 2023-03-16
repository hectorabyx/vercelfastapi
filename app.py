from fastapi import FastAPI
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain



question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

#response = llm_chain.run(question)
app = FastAPI()
@app.get("/")
def index():
    return {"message": question}
