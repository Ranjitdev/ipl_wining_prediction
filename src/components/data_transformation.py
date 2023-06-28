from src.logger import logging
from src.exception import CustomException
from src.pipeline.transformation_pipeline import DataTransformationPipe
from src.utils import save_obj, load_obj
import sys
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataTransformationConfig:
    preprocessor = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig

    def save_data_transformation(self, data):
        try:
            data = data.sample(axis=0, frac=1, random_state=51)
            transform_obj = DataTransformationPipe().data_transform_pipe()
            x = data.drop('Result', axis=1)
            y = data.iloc[:, -1]
            transform_obj.fit(x)
            save_obj(transform_obj, self.config.preprocessor)
            logging.info('Data transformer saved successfully')
            return x, y
        except Exception as e:
            raise CustomException(e, sys)

    def transform_data(self, x, y):
        try:
            x_train, x_test, y_train, y_test = train_test_split(
                x, y, train_size=0.8, random_state=41
            )
            transform_data = load_obj(
                self.config.preprocessor
            )
            train_array = transform_data.fit_transform(
                x_train
            )
            test_array = transform_data.transform(
                x_test
            )
            logging.info('Data transformed and returned')
            return train_array, test_array, y_train, y_test
        except Exception as e:
            raise CustomException(e, sys)
