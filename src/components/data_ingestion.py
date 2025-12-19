import sys
from pathlib import Path
PROJECT_ROOT = Path.cwd()
sys.path.insert(0, str(PROJECT_ROOT))
import os
print("current w d is project root: \n",os.getcwd())

from box.exceptions  import BoxValueError
import pandas as pd
import logging
from src.config.configuration import DataIngestionConfig,ConfigurationManager

# component to load the data
class DataIngestionLoader:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
        
    def load_data(self):
        # load from source url if source url is given
        if self.config.source_url:
            logging.info(f"Loading data from source url: {self.config.source_url}")
            try:
                df = pd.read_csv(self.config.source_url)
                logging.info(f"Data read successfully from {self.config.source_url}")
            except Exception as e:
                logging.info(f"Error reading CSV file from source url: {e}")
                raise BoxValueError(f"Error reading CSV file: {e}")
        else:
            # load from local data file
            try:
                logging.info(f"Loading data from local file: {self.config.local_data_file}")
                df = pd.read_csv(self.config.local_data_file)
            except Exception as e:
                logging.info(f"Error reading CSV file from local file: {e}")
                raise BoxValueError(f"Error reading csv file: {e}")
        return df

    def save_data(self,df:pd.DataFrame):
        try:
            os.makedirs(self.config.root_dir,exist_ok=True)
            filename = (self.config.local_data_file).split("/")[-1]
            print("filename to save: ",filename)
            logging.info(f"Saving data to {os.path.join(self.config.root_dir,filename)}")
            df.to_csv(os.path.join(self.config.root_dir,filename), index=False)
            logging.info(f"Data saved successfully at {os.path.join(self.config.root_dir,filename)}")
        except Exception as e:
            logging.info(f"Error saving data: {e}")
            raise BoxValueError(f"Error saving data: {e}")

# ingestion executor
class DataIngestionExecutor:
    def __init__(self):
        conf_manager = ConfigurationManager()
        self.config = conf_manager.get_data_ingestion_config()
        self.data_loader = DataIngestionLoader(self.config)
    def execute_data_ingestion(self)->pd.DataFrame:
        logging.info("Data ingestion execution started")
        df = self.data_loader.load_data()
        logging.info("Data ingestion process completed")
        logging.info(f"Data Shape: {df.shape}")
        logging.info(f"Data cols: {df.columns}")
        logging.info(f"Df Dtypes: {df.dtypes}")
        logging.info(f"Data Head: {df.head()}")
        self.data_loader.save_data(df)
        logging.info("Data saved successfully after ingestion")
        return df


if __name__ == "__main__":
    ingestion_executor =  DataIngestionExecutor()
    df  = ingestion_executor.execute_data_ingestion()
    
