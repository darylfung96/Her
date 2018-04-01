import numpy as np

from src.data_utils.preprocessing_helper import get_reverse_contractions

class TokenizerWrapper:

    def __init__(self, tokenizer):
        """

        :param tokenizer: a function that can be called right away to tokenize text
                            e.g: tokenizer('hey how are you')  -> ['hey', 'how', 'are', 'you']
        """
        self.tokenizer = tokenizer


    def tokenize(self, texts):
        """
        the main helper is in _tokenize_text
        This function helps to delegate task and choose the function between a function that deals with a single string
        or a list of string

        :param texts:   A list of string or a single string
        :return:        tokenized text
        """
        if type(texts) == str:
            return self._tokenize_text(texts)
        else:
            return self._tokenize_array(texts)


    def _tokenize_array(self, texts):
        assert type(texts) in (np.ndarray, list)

        return [self._tokenize_text(text) for text in texts]

    def _tokenize_text(self, sentence: str):
        """

        :param text: string
        :return:
        """
        if type(sentence) not in (str, np.str_):
            raise TypeError('value passed into tokenize_text has to be a string')

        reverse_contractions = get_reverse_contractions()

        for key, value in reverse_contractions.items():
            sentence = sentence.replace(key, value)

        texts = self.tokenizer(sentence)

        return texts
