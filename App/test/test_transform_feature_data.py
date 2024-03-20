from ..transform_feature_data import predict, predict_over_range_of_values, get_varying_change_range, is_row_today

import unittest
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd


class TestTransformFeatureData(unittest.TestCase):
    
    
    def test_get_varying_change_range(self):
        PRICE_CHANGE_INTERVAL = 0.1
        
        stock = yf.Ticker("SHB-A.ST")
        data = stock.history(period="1d")
        price = data["Open"].iloc[0]

        self.assertEqual(get_varying_change_range(stock), price * PRICE_CHANGE_INTERVAL)



    def test_is_row_today_should_be_same(self):
        date_str = datetime.now().strftime('%Y-%m-%d')
        date = pd.date_range(date_str, periods=1, freq="d")
        
        self.assertTrue(is_row_today(date))
        

    
    def test_is_row_today_should_not_be_same(self):
        date_str = datetime.now() - timedelta(1)
        datetime.strftime(date_str, '%Y-%m-%d')
        date = pd.date_range(date_str, periods=1, freq="d")
        
        self.assertFalse(is_row_today(date))


if __name__ == "__main__":
    unittest.main()