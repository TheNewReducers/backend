from fastapi import FastAPI, UploadFile
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

import controller
import image_processing

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

@app.get("/test/")
async def test():
   return str(image_processing.test())


@app.get("/categories")
async def return_all_categories():
    return None
