import tarfile
import urllib.request as request
import pandas as pd


class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download(self):
        URL = self.config.raw_data_URL
        tarfile_name = self.config.tar_filepath
        request.urlretrieve(URL, tarfile_name)
    
    def extract_file(self):
        with tarfile.open(self.config.tar_filepath) as tar_f:
            tar_f.extractall(self.config.untar_filepath)

    def prepare(self):
        with open(f"{self.config.untar_filepath}/CaliforniaHousing/cal_housing.domain", 'r') as f:
            content = f.readlines()

        self.col_name = [col.split(':')[0] for col in content]

        self.df = pd.read_csv(f"{self.config.untar_filepath}/CaliforniaHousing/cal_housing.data", sep=",", names=self.col_name)

    def save_data(self):
        self.df.to_csv(self.config.prepared_datapath,index=False)