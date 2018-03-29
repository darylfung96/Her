import unittest

from src.data_utils import TwitterDataset

class TwitterDatasetTest(unittest.TestCase):

    def test_retrieve_data(self):
        dataset = TwitterDataset()
        data = dataset.get_raw_data

        self.assertTrue(data is not None)
        self.assertTrue(data[0] is not None)

    def test_preprocess_data(self):
        dataset = TwitterDataset()
        preprocessed_data = dataset.get_preprocessed_data

        self.assertTrue(preprocessed_data is not None)
        self.assertTrue(preprocessed_data[0] is not None)


if __name__ == '__main__':
    unittest.main()