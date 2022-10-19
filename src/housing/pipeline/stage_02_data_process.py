from housing.config import ConfigurationManager
from housing.components import DataProcess

config = ConfigurationManager()
data_process_config = config.get_data_process_config()
data_process = DataProcess(data_process_config)
data_process.read_data()
data_process.split_data()
data_process.transform_data()
data_process.save_scaler_pickle()
data_process.save_split_data()