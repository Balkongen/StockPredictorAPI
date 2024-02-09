from fastapi import FastAPI, Response, status
from .service import *
from .Ticker import Ticker


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/prediction/{ticker}", status_code=status.HTTP_200_OK)
async def get_ml_prediction(ticker: Ticker):
    return ticker + " : price breaking point: " + get_prediction(ticker)



# @app.get("/ml")
# async def get_ml_prediction():
#     return get_prediction()
