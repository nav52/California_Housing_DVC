from housing.config import ConfigurationManager
from housing.components import ModelTrain

config = ConfigurationManager()
model_train_config = config.get_model_train_config()
model_train = ModelTrain(model_train_config)
model_train.read_train_data()
model_train.train_model()
model_train.save_model_pickle()