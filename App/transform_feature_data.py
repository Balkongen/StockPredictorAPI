import joblib
import numpy as np
import pandas as pd

import yfinance as yf

def predict(ticker): # TODO make this take in a int as paremter for change value?

    model = joblib.load("App/Models/model_RF_" + ticker + ".pkl")
    
    features = __transform_features(ticker)

    input_data = np.insert(features.values, 0, 55)
    
    prediction = model.predict(np.array(input_data).reshape(1, -1)) 
    
    return prediction


def predict_over_range_of_values(ticker):
    model = joblib.load("App/Models/model_RF_" + ticker + ".pkl")
    
    features = __transform_features(ticker)
    varying_input_values = np.linspace(-10, 10, 100)  # Adjust the range and number of points as needed

    for varying_input in varying_input_values:
        
        input_data = np.insert(features.values, 0, varying_input)
        prediction = model.predict(np.array(input_data).reshape(1, -1))  # Reshape for single sample

        if prediction[0] == 1:
            return varying_input;



def __transform_features(ticker): # TODO naming convetion for private/help method??
    
    SHORT_CHANGE_HORIZON = 5
    MID_CHANGE_HORIZON = 20
    LONG_CHANGE_HORIZON = 50

    stock = yf.Ticker(ticker)

    data = stock.history(period="6mo").iloc[::-1]

    data["Short_day_change"] = (data["Close"] - data["Close"].shift(-SHORT_CHANGE_HORIZON)) / SHORT_CHANGE_HORIZON
    data["Mid_day_change"] = (data["Close"] - data["Close"].shift(-MID_CHANGE_HORIZON)) / MID_CHANGE_HORIZON
    data["Long_day_change"] = (data["Close"] - data["Close"].shift(-LONG_CHANGE_HORIZON)) / LONG_CHANGE_HORIZON

    features = data[["Short_day_change", "Mid_day_change", "Long_day_change"]].iloc[0]
    
    return features



def get_varying_change_range(stock):
    PRICE_CHANGE_INTERVAL = 0.1

    data = stock.history(period="1d")
    price = data["Open"].iloc[0]
    return price * PRICE_CHANGE_INTERVAL