# Create a new file: models/schemas.py
from pydantic import BaseModel
from models import ResponseSignal


class UploadResponse(BaseModel):
    signal: str
    project_id: str | None = None
    filename: str | None = None

    class Config:
        use_enum_values = True  # Automatically convert enums to values