from fastapi import FastAPI

# app = FastAPI()
#
#
# @app.get("/api/v1/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/api/v1/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#-------------------------------------
# from fastapi import FastAPI
#
# from routes import base
# app = FastAPI()
#
# app.include_router(base.base_router)
#------------------------------------
from fastapi import FastAPI
from routes import base
from routes import data

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)