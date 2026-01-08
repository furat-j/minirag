from fastapi import FastAPI

app = FastAPI()


@app.get("api/v1/")
async def root():
    return {"message": "Hello World"}


@app.get("api/v1/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
