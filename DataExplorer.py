import pandas


class DataExplorer:
    def __init__(self):
        pandas.set_option("display.max.columns", None)

    # Prints main info about dataframe using given columns
    def describe(self, df):
        print(df.describe())

    def info(self, df):
        print(df.info())