import unittest

from src.data_utils.preprocessing_helper import get_contractions, get_reverse_contractions


class PreprocessingHelperTest(unittest.TestCase):

    def test_get_contractions(self):
        contractions = get_contractions()
        self.assertTrue(type(contractions) is dict)
        self.assertTrue(contractions.get("aren't") is not None)

        self.assertTrue(contractions.get("hello") is None)
        self.assertTrue(contractions.get("") is None)


    def test_get_reverse_contractions(self):
        reverse_contractions = get_reverse_contractions()
        self.assertTrue(type(reverse_contractions) is dict)
        self.assertTrue(reverse_contractions.get("let us") is not None)

        self.assertTrue(reverse_contractions.get("aren't") is None)
        self.assertTrue(reverse_contractions.get("") is None)