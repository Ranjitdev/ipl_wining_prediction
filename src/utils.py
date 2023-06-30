from src.exception import CustomException
from src.logger import logging
from src.components.data_ingesion import DataInsgest
import sys
import os
import dill


def save_obj(obj, file):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, 'wb') as file:
        dill.dump(obj, file)
        logging.info(f'File saved {file}')


def load_obj(file):
    with open(file, 'rb') as file:
        logging.info(f'Loaded the file {file}')
        return dill.load(file)

def get_data():
    data, matches, tables = DataInsgest().initiate_ingesion()
    teams = list(data['Batting'].unique())
    venues = list(data['Venue'].unique())
