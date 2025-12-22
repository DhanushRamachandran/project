from dataclasses import dataclass
from pathlib import Path

# entity for data ingestion
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url:str
    local_data_fil: Path
    unzip_dir: Path


# data validation
@dataclass
class DataValidationConfig:
    ingested_data_path: Path
    root_dir: Path
    schema_file_path: Path
    validation_status_file_path: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    validated_data_path: Path
    trained_tran_data_path: Path
    test_data_path: Path 