from src.components.data_ingesion import DataInsgest
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class InitiateComponents:
    def __init__(self):
        pass

    def get_data(self):
        data, matches, tables = DataInsgest().initiate_ingesion()
        return data, matches, tables

    def transform_data(self, data, matches, tables):
        x, y = DataTransformation().save_data_transformation(data)
        x_train, x_test, y_train, y_test = DataTransformation().transform_data(x, y)
        return x_train, x_test, y_train, y_test

    def train_data(self, x_train, x_test, y_train, y_test):
        params = ModelTrainer(x_train, x_test, y_train, y_test).save_train_model()
        result = ModelTrainer(x_train, x_test, y_train, y_test).test_model()
        return result, params


if __name__ == '__main__':
    data, matches, tables = InitiateComponents().get_data()
    x_train, x_test, y_train, y_test = InitiateComponents(
    ).transform_data(data, matches, tables)
    result, params = InitiateComponents(
    ).train_data(x_train, x_test, y_train, y_test)
    print(result, params)
