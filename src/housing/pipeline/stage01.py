from housing.components import DataIngestion
from housing.config import ConfigurationManager

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingerstion_config()
data_ingestion = DataIngestion(config=data_ingestion_config)
data_ingestion.download()
data_ingestion.extract_file()
data_ingestion.prepare()
data_ingestion.save_data()