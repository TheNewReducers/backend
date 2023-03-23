from fastapi import FastAPI
import openai

openai.api_key = "sk-..."


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}