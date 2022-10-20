from housing.config import ConfigurationManager
from housing.components import ModelEvaluation

config = ConfigurationManager()
data_eval_config = config.get_model_eval_config()
data_evaluation = ModelEvaluation(data_eval_config)
data_evaluation.load_test_data()
data_evaluation.load_model()
data_evaluation.predict_values()
data_evaluation.evaluate_model()
data_evaluation.store_scores()