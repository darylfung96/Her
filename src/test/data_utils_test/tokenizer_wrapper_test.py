from nltk.tokenize import word_tokenize
import numpy as np
import unittest

from src.data_utils.tokenizer_wrapper import TokenizerWrapper


class TokenizerWrapperTest(unittest.TestCase):
    # TokenizerWrapper accepts a callable function that tokenizes right away
    tokenizer_wrapper = TokenizerWrapper(lambda string: string.split())

    def test_initialization(self):
        tokenizer_wrapper = TokenizerWrapper(lambda string: string.split())
        self.assertTrue(callable(tokenizer_wrapper.tokenizer))


    def test_tokenize(self):
        # test string split tokenizer
        tokenizer_wrapper = TokenizerWrapper(lambda string: string.split())
        tokenized_text = tokenizer_wrapper.tokenize('hello how are you')
        self.assertTrue(tokenized_text[0] == 'hello')
        self.assertTrue(tokenized_text[-1] == 'you')

        # test nltk tokenizer
        tokenizer_wrapper = TokenizerWrapper(word_tokenize)
        tokenized_text = tokenizer_wrapper.tokenize('hello how are you')
        self.assertTrue(tokenized_text[0] == 'hello')
        self.assertTrue(tokenized_text[-1] == 'you')

        # if an unknown character is passed in, it should return back the unknown character
        tokenized_text = tokenizer_wrapper.tokenize('a')
        self.assertFalse(tokenized_text[0] is None)


        """ test passing list or numpy array to tokenize function """
        tokenized_texts = tokenizer_wrapper.tokenize(['hello how are you', 'i am fine, thank you'])
        self.assertTrue(tokenized_texts[0][0] == 'hello')
        self.assertTrue(tokenized_texts[0][-1] == 'you')
        self.assertTrue(tokenized_texts[1][0] == "i'm")
        self.assertTrue(tokenized_texts[1][-1] == 'you')

        tokenized_texts = np.array(['hello how are you', 'i am fine, thank you'])
        tokenized_texts = tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertTrue(tokenized_texts[0][0] == 'hello')
        self.assertTrue(tokenized_texts[0][-1] == 'you')
        self.assertTrue(tokenized_texts[1][0] == "i'm")
        self.assertTrue(tokenized_texts[1][-1] == 'you')


        """ test edge cases"""
        tokenized_texts = "how is he doing there he said he did not do that then it is not his fault"
        tokenized_texts = tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertTrue(tokenized_texts[0] == "how's")
        self.assertTrue(tokenized_texts[-1] == "fault")

        tokenized_texts = "I would not ever want to would not play with would not"
        tokenized_texts = tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertTrue(tokenized_texts[0] == "i")
        self.assertTrue(tokenized_texts[-1] == "wouldn't")

        tokenized_texts = np.array([12,34])
        tokenize_test_type_error = lambda : tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertRaises(TypeError, tokenize_test_type_error)