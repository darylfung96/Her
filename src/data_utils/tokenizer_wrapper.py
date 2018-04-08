import numpy as np
import string

from src.data_utils.preprocessing_helper import get_abbreviations, get_prioritized_abbreviations

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

        sentence = sentence.lower()

        reverse_priortize_contractions = get_prioritized_abbreviations()
        reverse_contractions = get_abbreviations()

        tokens = self.tokenizer(sentence)

        contracted_tokens = self.__replace_words(tokens, reverse_priortize_contractions)
        contracted_tokens = self.__replace_words(contracted_tokens, reverse_contractions)

        return contracted_tokens



    def __replace_words(self, tokens, contractions: dict):
        contracted_tokens = []
        index = 0
        while index < len(tokens)-1:
            new_text = "{} {}".format(tokens[index], tokens[index + 1])
            new_text_no_punc = new_text.translate(new_text.maketrans("", "", string.punctuation))

            shorten_text = contractions.get(new_text_no_punc)

            if shorten_text:
                shorten_text = new_text.replace(new_text_no_punc, shorten_text)
                contracted_tokens.append(shorten_text)
                index += 2
            else:
                contracted_tokens.append(tokens[index])
                index += 1

        # when there is a leftover last word that wasn't added to the new contracted text, then we add it back in
        if index == len(tokens)-1:
            contracted_tokens.append(tokens[index])

        return contracted_tokens
