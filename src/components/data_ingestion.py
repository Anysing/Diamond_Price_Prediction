import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## Initialize the data ingestion configuration

@dataclass
class dataingestionconfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')

class dataingestion:
    def __init__(self):
        self.ingestion_config = dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data ingestion started')

        try:
            df = pd.read_csv(os.path.join('notebooks/Data','gemstone.csv'))
            logging.info('Dataset read as csv file')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info('Train Test split started')
            train_set,test_set = train_test_split(df,test_size = 0.30,random_state = 30)
            train_set.to_csv(self.ingestion_config.train_data_path,index=True,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = True,header = True)

            logging.info('Data ingestion is completed')

            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)

        except Exception as e:
            logging.info('Error in data ingestion configuration')
