import numpy as np

class TokenizerWrapper:

    def __init__(self, tokenizer):
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

    def _tokenize_text(self, text: str):
        """

        :param text: string
        :return:
        """
        pass