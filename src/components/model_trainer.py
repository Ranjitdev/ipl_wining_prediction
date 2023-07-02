import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.utils import save_obj, load_obj
import os
import sys
from dataclasses import dataclass

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings
warnings.simplefilter('ignore')


@dataclass
class ModelTrainerConfiguration:
    model = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self, x_train, x_test, y_train, y_test):
        self.config = ModelTrainerConfiguration
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def save_train_model(self):
        try:
            model = RandomForestClassifier()
            param = {
                # 'n_estimators': range(10, 100, 10),
                # 'criterion': ['gini', 'entropy', 'log_loss'],
                'max_depth': range(5, 15, 3),
                'min_samples_split': [6, 8, 10, 12],
                'min_samples_leaf': range(3, 10, 2),
                'max_features': ['sqrt', 'log2']
            }
            gs = GridSearchCV(
                model, param,
                scoring='accuracy',
                n_jobs=8, cv=5,
                error_score='raise',
                verbose=2
            )
            gs.fit(self.x_train, self.y_train)

            model.set_params(**gs.best_params_)
            model.fit(self.x_train, self.y_train)
            save_obj(
                model, self.config.model
            )
            logging.info(
                f'{str(model)} saved successfully with params {gs.best_params_}'
            )
            return gs.best_params_
        except Exception as e:
            raise CustomException(e, sys)

    def test_model(self):
        try:
            model = load_obj(
                self.config.model
            )
            train_pred = model.predict(self.x_train)
            train_score = np.round(
                accuracy_score(self.y_train, train_pred)*100, 2
            )
            test_pred = model.predict(self.x_test)
            test_score = np.round(
                accuracy_score(self.y_test, test_pred)*100, 2
            )

            result = {
                'Train score': [train_score],
                'Test score': [test_score]
            }
            result = pd.DataFrame(result)
            logging.info(
                f'Model tested Train score {train_score}, Test score {test_score}'
            )
            return result
        except Exception as e:
            raise CustomException(e, sys)
