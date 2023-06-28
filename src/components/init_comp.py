from src.components.data_ingesion import DataInsgest
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


data, matches, tables = DataInsgest().initiate_ingesion()
x, y = DataTransformation().save_data_transformation(data)
x_train, x_test, y_train, y_test = DataTransformation().transform_data(x, y)
params = ModelTrainer(x_train, x_test, y_train, y_test).save_train_model()
result = ModelTrainer(x_train, x_test, y_train, y_test).test_model()
print(result, params)
