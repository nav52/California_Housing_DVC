from sklearn.linear_model import LinearRegression
import pandas as pd
from numpy import loadtxt
import pickle


class ModelTrain:
    def __init__(self, config):
        self.config = config
    
    def read_train_data(self):
        train_X_datapath = self.config.train_X_datapath
        train_y_datapath = self.config.train_y_datapath
        self.X_train = loadtxt(train_X_datapath, delimiter=',')
        self.y_train = loadtxt(train_y_datapath, delimiter=',')

    def train_model(self):
        self.reg_model_1 = LinearRegression()
        self.reg_model_1.fit(self.X_train, self.y_train)

    def save_model_pickle(self):
        pickle.dump(self.reg_model_1, open(self.config.model_1_pickle_file,'wb'))
