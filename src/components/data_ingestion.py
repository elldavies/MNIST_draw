import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # define the paths for the data ingestion
    train_data_path : str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','raw_data.csv')

class DataIngestion:
    def __init__(self):
        # get the data ingestion configuration from data ingestion config class
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")
        try:
            # read in raw data from the raw data path
            df=pd.read_csv('data/raw_data.csv')

            # get the directory path for data folder from the ingestion config instance
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # write the raw data to csv (folder given by ingestion config)
            df.to_csv(self.ingestion_config.raw_data_path, index=False) 

            # get the test and train data from the raw data
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # write the test and train data to csv (folder given by ingestion config)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion complete")

            # return the train and test data paths
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys) 
        
if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()