from src.data_utils.data_utils_config import DATA_SETTINGS

class Dataset:
    def __init__(self, dataset_name, tokenizer):
        self._raw_data = None
        self._preprocessed_data = None

        self.filename = DATA_SETTINGS[dataset_name]

        """make sure that the type of tokenizer is TokenizerWrapper"""
        assert type(tokenizer).__name__ == 'TokenizerWrapper'
        self.tokenizer = tokenizer

    @property
    def get_raw_data(self):
        return self._raw_data

    @property
    def get_preprocessed_data(self):
        return self._preprocessed_data

    def retrieve_data(self):
        raise NotImplementedError('Must execute this function in subclasses')

    def preprocess_data(self):
        raise NotImplementedError('Must execute this function in subclasses')
