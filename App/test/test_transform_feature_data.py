import unittest
from ..transform_feature_data import predict, predict_over_range_of_values, get_varying_change_range

import yfinance as yf

class TestTransformFeatureData(unittest.TestCase):
    
    
    def test_get_varying_change_range(self):
        PRICE_CHANGE_INTERVAL = 0.1
        
        stock = yf.Ticker("SHB-A.ST")
        data = stock.history(period="1d")
        price = data["Open"].iloc[0]

        self.assertEqual(get_varying_change_range(stock), price * PRICE_CHANGE_INTERVAL)


if __name__ == "__main__":
    unittest.main()