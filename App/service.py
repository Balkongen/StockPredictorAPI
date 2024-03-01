from .transform_feature_data import predict

def get_prediction(ticker):
    return str(predict(ticker))
