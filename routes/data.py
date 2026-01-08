#
import os

from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
import aiofiles
from models import ResponseSignal

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["data", "api_v1"],
)

#___________________________________________________________
# @data_router.post("/upload/{project_id}")  # Added @ here!
# async def upload_data(
#         project_id: str,
#         file: UploadFile,
#         app_settings: Settings = Depends(get_settings)
# ):
#     is_valid, result_signal = DataController().validate_uploaded_file(file=file)
#     if not is_valid:
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
#                             content={
#                                 "signal": result_signal
#                             }
#                             )
#     project_dir_path = ProjectController().get_project_path(project_id=project_id)
#     file_path = os.path.join(project_dir_path,file.filename)
#
#
#     async with aiofiles.open(file_path, mode="wb") as f:
#         while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
#             await f.write(chunk)
#
#     return JSONResponse(status_code=status.HTTP_201_CREATED,
#                         content={
#                             "signal": ResponseSignal.FILE_UPLOADED_SUCCESS
#                         })


    # return {
    #     "message": "File uploaded successfully",
    #     "project_id": project_id,
    #     "filename": file.filename,
    #     "content_type": file.content_type
    # }
#_______________________________________________

from models.schemas import UploadResponse


@data_router.post("/upload/{project_id}", response_model=UploadResponse)
async def upload_data(
        project_id: str,
        file: UploadFile,
        app_settings: Settings = Depends(get_settings)
):
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal.value}
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = os.path.join(project_dir_path, file.filename)

    async with aiofiles.open(file_path, mode="wb") as f:
        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)

    return {
        "signal": ResponseSignal.FILE_UPLOADED_SUCCESS.value,
        "project_id": project_id,
        "filename": file.filename
    }