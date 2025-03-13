# predictions/ml_model.py

import numpy as np
from sklearn.linear_model import LinearRegression

class SuccessScoreModel:
    def __init__(self):
        self.model = LinearRegression()
        self.model.coef_ = np.array([0.30, 0.25, 0.15, 0.10, 0.08, 0.07, 0.05, 0.05, -0.10])
        self.model.intercept_ = 0  # Simplified intercept

    def predict(self, inputs):
        inputs_array = np.array([inputs])
        return self.model.predict(inputs_array)[0]