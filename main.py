from fastapi import FastAPI, UploadFile
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

import controller

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    file_process = file.file

    resp: dict = controller.file_input(file_process)
    print(type(resp))
    return resp


@app.get("/categories")
async def return_all_categories():
    return None
