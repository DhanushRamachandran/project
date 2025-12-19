import sys
from pathlib import Path
PROJECT_ROOT = Path.cwd()
sys.path.insert(0, str(PROJECT_ROOT))
import os
print("current w d: \n",os.getcwd())
from src.entity.config_entity  import DataValidationConfig
from dataclasses import dataclass
from src.constants import *
from src.utils.common import read_yaml,create_directories

class ValidationConfigManager:
    def __init__(self,config_path=CONFIG_FILE_PATH,
                 schema_path = SCHEMA_FILE_PATH
         #        params_path =  PARAMS_FILE_PATH
                 ):
        
        self.config = read_yaml(config_path) #val_config = self.config.
        self.val_config = self.config.data_validation
        self.ingestion_config = self.config.data_ingestion
        self.schema = read_yaml(schema_path)
        #self.params = read_yaml(params_path)

        print(self.val_config)
        print(self.schema)
        #print(self.params)

        new_possible_data_dirs = [self.val_config.root_dir,os.path.dirname(self.val_config.validation_status_file_path)]
        create_directories(new_possible_data_dirs)

    def get_data_validation_config(self) -> DataValidationConfig:

        data_val_config = DataValidationConfig(
            ingested_data_path = self.ingestion_config.root_dir,
            root_dir = self.val_config.root_dir,
            schema_file_path = self.val_config.schema_file_path,
            validation_status_file_path = self.val_config.validation_status_file_path,
            all_schema=self.schema
        )
        return data_val_config

# unit test
if __name__ == "__main__":
    config_manager = ValidationConfigManager()
    data_val_configs = config_manager.get_data_validation_config()
    print(data_val_configs)

