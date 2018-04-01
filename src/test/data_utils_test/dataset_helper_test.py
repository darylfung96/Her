import unittest
from unittest import TestCase
from nltk.tokenize import word_tokenize

from data_utils.dataset_helper import Dataset
from data_utils.data_utils_config import DATA_SETTINGS
from data_utils.tokenizer_wrapper import TokenizerWrapper

class DatasetTest(TestCase):
    tokenizer = TokenizerWrapper(word_tokenize)

    def test_dataset_structure(self):
        self.assertTrue(hasattr(Dataset, 'get_raw_data'))
        self.assertTrue(hasattr(Dataset, 'get_preprocessed_data'))
        self.assertTrue(hasattr(Dataset, 'retrieve_data'))
        self.assertTrue(hasattr(Dataset, 'preprocess_data'))

    def test_dataset_func(self):
        dataset = Dataset('twitter', self.tokenizer)
        self.assertRaises(NotImplementedError, dataset.retrieve_data)
        self.assertRaises(NotImplementedError, dataset.preprocess_data)

        self.assertEqual(dataset.get_raw_data, None, 'raw data should be None if we initialize from the superclass of dataset')
        self.assertEqual(dataset.get_preprocessed_data, None, 'preprocess data should be done if we intialize from the superclass of dataset')

    def test_init_dataset(self):
        data_name = 'twitter'
        dataset = Dataset(data_name, self.tokenizer)

        self.assertEqual(dataset.filename, DATA_SETTINGS[data_name], 'location directory test')


if __name__ == '__main__':
    unittest.main()