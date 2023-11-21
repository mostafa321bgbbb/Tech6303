import matplotlib.pyplot as plt
import pandas as pd

class Analyzer:
    def __init__(self) -> None:
        self.__data = None
    def read_dataset(self, fileName):
        self.__data  = pd.read_csv(fileName)
    def describe(self):
        print('numeric data description:')
        print(self.__data.describe())
        print('non numeric data description:')
        print(self.__data.describe(include='object'))
    def drop_missing_data(self):
        self.__data = self.__data.dropna()
    def plot_histograms_numeric(self, columnName):
        self.__data.hist(column=columnName, bins=50)
        plt.show()
    def retrieve_data(self):
        return self.__data
    def drop_columns(self, attribute_list):
        ########################To be implemented####################################
        pass
    def encode_features(self, columns_list):
        ########################To be implemented####################################
        pass
    def encode_label(self, label):
        ########################To be implemented####################################
        pass
    def shuffle(self):
        ########################To be implemented####################################
        pass
    def plot_correlationMatrix(self):
        ########################To be implemented####################################
        pass
    def plot_pairPlot(self):
        ########################To be implemented####################################
        pass
    def plot_histograms_categorical(self):
        ########################To be implemented####################################
        pass
    def plot_boxPlot(self):
        ########################To be implemented####################################
        pass