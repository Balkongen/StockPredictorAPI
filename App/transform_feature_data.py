import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import yfinance as yf

def train_model():

    model = joblib.load("App/model_RF.pkl")
    
    SHORT_CHANGE_HORIZON = 5
    MID_CHANGE_HORIZON = 20
    LONG_CHANGE_HORIZON = 50

    shb = yf.Ticker("SHB-A.ST")

    data = shb.history(period="6mo").iloc[::-1]

    data["Short_day_change"] = (data["Close"] - data["Close"].shift(-SHORT_CHANGE_HORIZON)) / SHORT_CHANGE_HORIZON
    data["Mid_day_change"] = (data["Close"] - data["Close"].shift(-MID_CHANGE_HORIZON)) / MID_CHANGE_HORIZON
    data["Long_day_change"] = (data["Close"] - data["Close"].shift(-LONG_CHANGE_HORIZON)) / LONG_CHANGE_HORIZON

    features = data[["Short_day_change", "Mid_day_change", "Long_day_change"]].iloc[0]

    input_data = np.insert(features.values, 0, 55)
    
    prediction = model.predict(np.array(input_data).reshape(1, -1)) 
    
    return prediction
