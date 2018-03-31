import os

from src.data_utils.dataset_helper import Dataset
from src.data_utils.preprocessing_helper import get_reverse_contractions


class TwitterDataset(Dataset):

    def __init__(self, tokenizer):
        super(TwitterDataset, self).__init__('twitter')
        self.tokenizer = tokenizer
        self.retrieve_data()
        self.preprocessed_data()


    def retrieve_data(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(dir, '../', '../', '../', 'data')
        data_file = os.path.join(data_path, self.filename)

        with open(data_file, 'r') as f:
            self._raw_data = f.read()


    def preprocessed_data(self):
        preprocessed_data = self._raw_data.split('\n')
        preprocessed_data = [self.tokenizer.tokenize(single_data) for single_data in preprocessed_data]
        reverse_contractions = get_reverse_contractions()


from nltk.tokenize import word_tokenize
TwitterDataset(word_tokenize())
