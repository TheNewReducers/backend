from fastapi import FastAPI, File, UploadFile
import controller

app = FastAPI()


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    file_process = file.file
    resp: dict = controller.file_input(file_process)
    return resp


@app.get("/categories")
async def return_all_categories():
    return ["Meat", "Pet Food", "Snacks", "Fruits", "Vegetables", "Dairy", "Beverages", "Tobacco", "Alcohol"]
