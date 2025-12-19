from src import logger
from src.config.configuration import ConfigurationManager,DataIngestionConfig
from src.components.data_ingestion import DataIngestionConfig,DataIngestionExecutor,DataIngestionLoader
from src.constants import *
from src.config.validation_configuration import *
from src.entity.config_entity import DataValidationConfig
from src.utils.common import read_yaml,create_directories
from src.components.data_validation import DataValidator,ValidationConfigManager
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionExecutor()
    data_ingestion.execute_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"error in stage {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    config_manager = ValidationConfigManager()
    data_val_configs = config_manager.get_data_validation_config()
    print(data_val_configs)
    validator = DataValidator(config=data_val_configs)
    validator.validate_data()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"error in stage {STAGE_NAME}: {e}")
    raise e
