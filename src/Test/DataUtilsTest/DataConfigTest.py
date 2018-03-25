import unittest

from src.DataUtils.DataConfig import DATA_SETTINGS

class DataConfigTest(unittest.TestCase):

    def test_data_settings(self):
        self.assertTrue(type(DATA_SETTINGS) is dict)
