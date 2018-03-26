import os

from src.DataUtils.Dataset import Dataset

class TwitterDataset(Dataset):

    def __init__(self):
        super(TwitterDataset, self).__init__('twitter')

        self.retrieve_data()
        self.preprocessed_data()


    def retrieve_data(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(dir, '../', '../', 'Data')
        data_file = os.path.join(data_path, self.filename)

        with open(data_file, 'r') as f:
            self._raw_data = f.read()


    def preprocessed_data(self):
        self._preprocessed_data = self._raw_data.split('\n')

        self._preprocessed_data = [data.replace('%amp; ', '') for data in self._preprocessed_data]
        self._preprocessed_data = [data.replace('%gt; ', '') for data in self._preprocessed_data]

TwitterDataset()