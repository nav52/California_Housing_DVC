import pickle
from pathlib import Path
from numpy import loadtxt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from housing.utils import save_json

class ModelEvaluation:
    def __init__(self,config):
        self.config = config
    
    def load_test_data(self):
        self.test_X_data = loadtxt(self.config.test_X_datapath, delimiter=',')
        self.test_y_data = loadtxt(self.config.test_y_datapath , delimiter=',')

    def load_model(self):
        self.regmodel = pickle.load(open(self.config.model_1_pickle_file, 'rb'))

    def predict_values(self):
        self.predicted_values = self.regmodel.predict(self.test_X_data)

    def evaluate_model(self):
        self.scores = {}
        self.scores["Mean Absolute Error"] = mean_absolute_error(self.test_y_data, self.predicted_values)
        self.scores["Mean Squared Error"] = mean_squared_error(self.test_y_data, self.predicted_values)
        self.scores["R2 score"] = r2_score(self.test_y_data, self.predicted_values)

    def store_scores(self):
        save_json(Path(self.config.scores_file), self.scores)
        

