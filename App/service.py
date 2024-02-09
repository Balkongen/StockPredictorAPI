from .transform_feature_data import train_model

def get_prediction(ticker):
    return str(train_model(ticker))
