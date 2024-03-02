import unittest
from transform_feature_data import predict, predict_over_range_of_values

class TestTransformFeatureData(unittest.TestCase):
    
    def test__transform_features(self):
        features = predict("SHB-A.ST")

        print(features)


if __name__ == "__main__":
    unittest.main()