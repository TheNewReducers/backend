from fastapi import FastAPI, UploadFile
import openai
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

openai.api_key = "sk-..."

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}



