import sys
from pathlib import Path
PROJECT_ROOT = Path.cwd()
sys.path.insert(0, str(PROJECT_ROOT))
import os
print("current w d: \n",os.getcwd())
from dataclasses import dataclass
from pathlib import Path 
from src.constants import *
from src.utils.common import *
from pathlib import Path 

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

class ConfigurationManager:
    def __init__(self,config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH ):
        print(config_file_path)
        self.configs = read_yaml(config_file_path)
        #self.params = read_yaml_file(params_file_path)
        #self.schema = read_yaml_file(schema_file_path)
        create_directories([self.configs.artifact_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.configs.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    

# unit test
if __name__ == "__main__":
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    print(data_ingestion_config)
