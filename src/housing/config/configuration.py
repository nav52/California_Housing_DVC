from pathlib import Path
from housing.utils import read_yaml, create_directories
from housing.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from housing.entity import DataIngestionConfig, DataProcessConfig

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath: Path=CONFIG_FILE_PATH,
        params_filepath: Path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingerstion_config(self):
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            raw_data_URL=config.raw_data_URL,
            tar_filepath=config.tar_filepath,
            untar_filepath=config.untar_filepath,
            prepared_datapath=config.prepared_datapath
        )
        return data_ingestion_config
    
    def get_data_process_config(self):
        config = self.config.data_process
        create_directories([config.root_dir])
        data_process_config = DataProcessConfig(
            root_dir=config.root_dir,
            data_filepath=config.data_filepath,
            scaled_pickle_file=config.scaled_pickle_file
        )
        return data_process_config