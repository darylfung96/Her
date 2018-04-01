import unittest
import numpy as np
from nltk.tokenize.simple import string_span_tokenize

from src.data_utils import TwitterDataset
from src.data_utils.tokenizer_wrapper import TokenizerWrapper

class TwitterDatasetTest(unittest.TestCase):
    dataset = TwitterDataset(TokenizerWrapper(lambda string: string.split()), twitter_filename='twitter_test')


    def test_retrieve_data(self):
        data = self.dataset.get_raw_data

        self.assertTrue(data is not None)
        self.assertTrue(data[0] is not None)

    def test_preprocess_data(self):
        preprocessed_data = self.dataset.get_preprocessed_data

        self.assertTrue(type(preprocessed_data) in (np.ndarray, list))
        self.assertTrue(preprocessed_data is not None)
        self.assertTrue(preprocessed_data[0] is not None)


if __name__ == '__main__':
    unittest.main()