from src.logger import logging
from src.exception import CustomException
from src.components.data_ingesion import DataInsgest
import sys
import os
from dataclasses import dataclass

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline, Pipeline


@dataclass
class DataPipeConfig:
    data, matches, tables = DataInsgest().initiate_ingesion()


class DataTransformationPipe:
    def __init__(self):
        self.config = DataPipeConfig()

    def data_transform_pipe(self):
        num_cols = ['Runs_left', 'Balls_left', 'Wicket_left', 'Total_run', 'crr', 'rrr']
        cat_cols = ['Batting', 'Bowling', 'Venue']
        num_pipe = make_pipeline(
            SimpleImputer(strategy='median'),
            StandardScaler()
        )
        cat_pipe = make_pipeline(
            SimpleImputer(strategy='most_frequent'),
            OneHotEncoder()
        )
        transform_obj = ColumnTransformer([
            ('num_pipe', num_pipe, num_cols),
            ('cat_pipe', cat_pipe, cat_cols)
        ], remainder='passthrough')
        return transform_obj


