from fastapi import FastAPI
from .service import *
from .Ticker import Ticker


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/prediction/{ticker}")
async def get_ml_prediction(ticker: Ticker):
    if (ticker is Ticker.SHB):
        return "HEJ: " + get_prediction()



# @app.get("/ml")
# async def get_ml_prediction():
#     return get_prediction()
