from src.constants import *
from src.utils.common import read_yaml,create_directories
from src.entity.config_entity import DataTransformationConfig
import logging

class TransformationConfigurationManager:

    def __init__(self, schema_file_path=SCHEMA_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 config_file_path = CONFIG_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        # create possible directpries required
        possible_directories = [self.config.data_transformation.root_dir]
        create_directories(possible_directories)

    def get_transformation_config(self):
        # load into oraganized data class for further steps
        transformation_config = DataTransformationConfig(
            root_dir=self.config.data_transformation.root_dir,
            validated_data_path=self.config.data_transformation.validated_data_path ,
            test_data_path=self.config.data_transformation.transformed_test_data_path ,
            trained_tran_data_path=self.config.data_transformation.transformed_train_data_path
        )
        return transformation_config


# unit test
if __name__ == "__main__":
    transformation_manager = TransformationConfigurationManager()
    transformation_configs = transformation_manager.get_transformation_config()
    print("The configs are : ",transformation_configs)
    logging.info("UNIT TEST - The configs are : ",transformation_configs)

