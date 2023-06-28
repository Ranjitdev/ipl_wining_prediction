import mysql.connector
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import sys
import os

ipl = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678rk",
    database='ipl'
)
cursor = ipl.cursor()
from sqlalchemy import create_engine
engine = create_engine(
    "mysql+pymysql://" + "root" + ":"
    + "12345678rk" + "@" + "localhost" + ":"
    + "3306" + "/" + "ipl" + "?" + "charset=utf8mb4"
)
con = engine.connect()


@dataclass
class DataIngesionConfig:
    cursor.execute('show tables')
    tables = cursor.fetchall()
    logging.info(f'Found {tables} data tables on database')
    db_data = pd.read_sql('model_data', con, index_col=None)
    logging.info('Data loaded from database')
    db_matches = pd.read_sql('matches', con, index_col=None)
    logging.info('Matches loaded from database')
    data_folder = os.path.join('artifacts')
    local_data_file = os.path.join('artifacts', 'data.csv')
    local_matches_file = os.path.join('artifacts', 'matches.csv')


class DataInsgest:
    def __init__(self):
        self.config = DataIngesionConfig()
        os.makedirs(self.config.data_folder, exist_ok=True)

    def initiate_ingesion(self):
        try:
            tables = self.config.tables
            data = self.config.db_data
            matches = self.config.db_matches
            data.to_csv(self.config.local_data_file)
            data.to_csv(self.config.local_matches_file)
            return data, matches, tables
        except Exception as e:
            raise CustomException(e, sys)
