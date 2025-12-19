import sys
from pathlib import Path
PROJECT_ROOT = Path.cwd()
sys.path.insert(0, str(PROJECT_ROOT))
import os
print("current w d: \n",os.getcwd())
# load the validation configs and schemas
from src.constants import *
from src.config.validation_configuration import *
from src.entity.config_entity import DataValidationConfig
from src.utils.common import read_yaml,create_directories
import pandas as pd
from box import ConfigBox
import logging

# perform the validation
class DataValidator:    
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self):
        logging.info("Initiating Data Validation")
        schema = self.config.all_schema["schema"]
        logging.info(f"Loaded schema (expected): {schema}")
        ingested_filename = os.listdir(self.config.ingested_data_path)[0]
        data = pd.read_csv(os.path.join(self.config.ingested_data_path,ingested_filename))
        
        with open(self.config.validation_status_file_path,"w") as f:
            for column in schema.keys():
                print(schema[column])
                expected_type = schema[column]['dtype']
                actual_type = data[column].dtype
                if expected_type != actual_type:
                    logging.error(f"Column '{column}' has an unexpected data type. Expected: {expected_type}, Actual: {actual_type}")
                    f.write(f"Column '{column}' has an unexpected data type. Expected: {expected_type}, Actual: {actual_type}\n")
                    raise ValueError(f"Column '{column}' has an unexpected data type. Expected: {expected_type}, Actual: {actual_type}")
                else:
                    logging.info(f"Column '{column}' has the expected data type. Expected: {expected_type}, Actual: {actual_type}")
                    f.write(f"Column '{column}' has the expected data type. Expected: {expected_type}, Actual: {actual_type}\n")

        f.close()
        logging.info("Data Validation Completed")

if __name__ == "__main__":
    config_manager = ValidationConfigManager()
    data_val_configs = config_manager.get_data_validation_config()
    print(data_val_configs)
    validator = DataValidator(config=data_val_configs)
    validator.validate_data()

            