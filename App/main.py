from fastapi import FastAPI
from .service import *
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/ml")
async def get_ml_prediction():
    return get_prediction()
