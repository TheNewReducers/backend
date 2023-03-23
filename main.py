from fastapi import FastAPI, UploadFile
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

import controller

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):

    file_process = file.file

    resp = controller.file_input(file_process)

    return {
        "filename": file.filename,
        "output": resp
    }


@app.get("/categories")
async def return_all_categories():
    return None
