import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class DataProcess:
    def __init__(self, config):
        self.config = config
    
    def read_data(self):
        data_filepath = self.config.data_filepath
        self.df = pd.read_csv(data_filepath, sep=',')

    def split_data(self):
        self.X = self.df.iloc[:,:-1]
        self.y = self.df.iloc[:,-1]
        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

    def transform_data(self):
        self.scaler=StandardScaler()
        self.scaler.fit_transform(self.X_train)
        self.scaler.transform(self.X_test)

    def save_scaler_pickle(self):
        pickle.dump(self.scaler, open(self.config.scaled_pickle_file, 'wb'))