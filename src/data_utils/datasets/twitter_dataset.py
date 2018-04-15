import os

from src.data_utils.dataset_helper import Dataset


class TwitterDataset(Dataset):

    def __init__(self, tokenizer, twitter_filename='twitter'):
        super(TwitterDataset, self).__init__(twitter_filename, tokenizer)

        self.inputs = []
        self.targets = []

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

        self._preprocessed_data = preprocessed_data

        self.inputs = preprocessed_data[::2]
        self.targets = preprocessed_data[1::2]

        shorter_length = min(len(self.inputs), len(self.targets))
        self.inputs = self.inputs[:shorter_length]
        self.targets = self.targets[:shorter_length]


