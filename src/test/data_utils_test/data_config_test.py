import unittest

from src.data_utils.data_utils_config import DATA_SETTINGS

class DataConfigTest(unittest.TestCase):

    def test_data_settings(self):
        self.assertTrue(type(DATA_SETTINGS) is dict)
