
from .BaseController import BaseController
from fastapi import UploadFile


class DataController(BaseController):
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file: UploadFile):
        # Check content type
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False

        # Check file size (FILE_MAX_SIZE is already in bytes from config)
        if file.size and file.size > self.app_settings.FILE_MAX_SIZE:
            return False

        return True