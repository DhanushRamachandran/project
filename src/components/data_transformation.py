import sys
from pathlib import Path
PROJECT_ROOT = Path.cwd()
sys.path.insert(0, str(PROJECT_ROOT))
import os
print("current w d is project root: \n",os.getcwd())
from src.config.transformation_configuration import transformation_configs
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
import os

class DataTransformer:
    def __init__(self,data_path):

        try:
            self.df = pd.read_csv(data_path)
            logging.info(f"Data {data_path} successfully loaded")
            logging.info(f"Data.head(): ",self.df.head())
            logging.info(f"Current columns: ",self.df.columns)
        except Exception as e:
            print(f"Exception occured in data loading: {e}")
            logging.info(f"Exception occured in data loading: {e}")

    def transform(self):
        X = self.df.drop["quality"]
        y = self.df["quality"]
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
        return [X_train,X_test,y_train,y_test]

    def save_transformed_data(self,X_train,y_train,X_test,y_test):
        train_path = transformation_configs.trained_tran_data_path
        test_path = transformation_configs.test_data_path
        dir_name = os.path.dirname(train_path)
        X_train.to_csv(os.path.join(dir_name,"X_train.csv"))
        X_test.to_csv(os.path.join(dir_name,"X_test.csv"))
        y_train.to_csv(os.path.join(dir_name,"y_train.csv"))
        y_test.to_csv(os.path.join(dir_name,"y_test.csv"))

# unit test
if __name__=="__main__":
    transformer = DataTransformer(transformation_configs.validated_data_path)
    transformed_data = transformer.transform()
    (X_train,X_test,y_train,y_test) = tuple(transformer)
    transformer.save_transformed_data(X_train,y_train,X_test,y_test)
