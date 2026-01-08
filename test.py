# test_settings.py
from helpers.config import get_settings

settings = get_settings()
print(f"App Name: {settings.APP_NAME}")
print(f"App Version: {settings.APP_VERSION}")
print(f"Allowed Types: {settings.FILE_ALLOWED_TYPES}")