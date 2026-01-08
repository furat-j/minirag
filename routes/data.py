# from fastapi import FastAPI, APIRouter, Depends, UploadFile
# # import os
# # from h11 import Data
# from helpers.config import get_settings, Settings
# from controllers import DataController
#
# data_router = APIRouter(
#     prefix="/api/v1/data",
#     tags=["data","api_v1"],
# )
#
# data_router.post("/upload/{project_id}")
# async def upload_data(project_id: str, file: UploadFile,
#                       app_settings: Settings = Depends(get_settings) ):
#
#         is_valid = DataController().validate_uploaded_file(file = file)
#         return is_valid

from fastapi import APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["data", "api_v1"],
)


@data_router.post("/upload/{project_id}")  # Added @ here!
async def upload_data(
        project_id: str,
        file: UploadFile,
        app_settings: Settings = Depends(get_settings)
):
    is_valid = DataController().validate_uploaded_file(file=file)
    if not is_valid:
        return {"error": "Invalid file", "project_id": project_id}

    return {
        "message": "File uploaded successfully",
        "project_id": project_id,
        "filename": file.filename,
        "content_type": file.content_type
    }