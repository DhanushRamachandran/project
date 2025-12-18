import os  
from pathlib import Path
import logging
from src.datascience_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError 
import yaml
from typing import List


def read_yaml_file(file_path: Path) -> ConfigBox:
    """ Reads a YAMl file and returns it as a config box object """
    try:
        content = yaml.safe_load(file_path)
        logging.info(f"yaml file: {file_path} is loaded successfully")
        return ConfigBox(content)
    except BoxValueError as box_exception:
        raise box_exception
    except Exception as e:
        raise e
    
@ensure_annotations   
def create_directories(dirs: list): 
    for dir in dirs:
        try:
            os.makedirs(dir,exist_ok=True)
            logger.info(f"created directory at : {dir}")
        except Exception as e:
            logger.info(f"error in creating directory at: {dir}\n error: {e}")
            raise e    
        except BoxValueError as box_exception:
            logger.info(f"error  in creating directory at: {dir}\n error: {box_exception}")
            raise  box_exception
        
@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path,"w") as json_file:
        json.dump(data,json_file,indent=4)
        logger.info(f"saved json file at : {path}")


@ensure_annotations
def save_bin(data:object, path:Path):
    try:
        joblib.dump(data,path)
        logger.info(f"saved binary file at : {path}")
    except Exception as e:
        logger.info(f"error in saving binary file at : {path}\n error: {e}")
        raise e
