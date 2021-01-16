import numpy
import pandas as pandas

TRAIN_DATA_PATH = 'resources\\train.csv'
TEST_DATA_PATH = 'resources\\test.csv'


# This class is used for loading, normalizing and getting train/test data from the CSV file
class DataLoader:
    train_data = None
    test_data = None

    def __load_data(self, data_path):
        return pandas.read_csv(data_path)

    def load_and_normalize_data(self):
        self.train_data = self.__load_data(TRAIN_DATA_PATH)
        self.test_data = self.__load_data(TEST_DATA_PATH)

        self.__normalize_data()

    # Normalize data and fills data gaps
    def __normalize_data(self):
        self.train_data.interpolate(method='linear', limit_direction='forward')
        self.test_data.interpolate(method='linear', limit_direction='forward')

        cat_columns = self.__get_categorical_columns()
        for c in cat_columns:
            self.train_data[c] = self.train_data[c].astype('category')
            self.test_data[c] = self.test_data[c].astype('category')
            self.train_data[c] = self.train_data[c].cat.codes
            self.test_data[c] = self.test_data[c].cat.codes

    def get_train_data(self):
        if self.train_data is None:
            raise Exception('Error while getting train data. Data has not been loaded yet.')

        return self.train_data

    def get_test_data(self):
        if self.test_data is None:
            raise Exception('Error while getting test data. Data has not been loaded yet.')

        return self.test_data

    def __get_categorical_columns(self):
        column_dict = dict(self.train_data.dtypes)
        object_columns = []

        for column, c_type in column_dict.items():
            if c_type == numpy.object:
                object_columns.append(column)

        return object_columns

# loader = DataLoader()
#
# loader.load_and_normalize_data()
# train_data = loader.get_train_data()
# test_data = loader.get_test_data()
#
# train_data.info()
