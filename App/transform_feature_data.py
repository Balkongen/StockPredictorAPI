import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def train_model():

    model = joblib.load("App/model_RF.pkl")

    column_order = ['Date', 'Bid', 'Ask', 'Opening price', 'High price', 'Low price', 'Closing price', 'Average price', 'Total volume', 'Turnover', 'Trades']
    data = pd.read_csv("App/SHB_A-1987-01-02-2023-09-08.csv", sep=";", decimal=",", skiprows=1, usecols=column_order)

    columns_to_drop = ["Bid", "Ask", "Opening price", "Average price"]
    data = data.set_index("Date").drop(columns=columns_to_drop)

    data.drop(data.index[100:], inplace=True)

    SHORT_CHANGE_HORIZON = 5
    MID_CHANGE_HORIZON = 20
    LONG_CHANGE_HORIZON = 50

    data["Short_day_change"] = (data["Closing price"] - data["Closing price"].shift(-SHORT_CHANGE_HORIZON)) / SHORT_CHANGE_HORIZON
    data["Mid_day_change"] = (data["Closing price"] - data["Closing price"].shift(-MID_CHANGE_HORIZON)) / MID_CHANGE_HORIZON
    data["Long_day_change"] = (data["Closing price"] - data["Closing price"].shift(-LONG_CHANGE_HORIZON)) / LONG_CHANGE_HORIZON

    features = data[["Short_day_change", "Mid_day_change", "Long_day_change"]].iloc[0]
    input_data = np.insert(features.values, 0, 0)
    prediction = model.predict(np.array(input_data).reshape(1, -1)) 

    return prediction