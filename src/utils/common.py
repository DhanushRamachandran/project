import os  
from pathlib import Path
import logging
from src import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError 
import yaml
from typing import List

def read_yaml(file_path:Path) -> ConfigBox:
    """ Reads a YAMl file and returns it as a config box object """
    print("reading yaml file: ",file_path)
    try:
        with open(file_path,"r") as yaml_file:
            print("file path: ",file_path)
            content = yaml.safe_load(yaml_file) 
            logger.info(f"yaml file: {file_path} is loaded successfully")
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
            logging.info(f"created directory at : {dir}")
        except Exception as e:
            logging.info(f"error in creating directory at: {dir}\n error: {e}")
            raise e    
        except BoxValueError as box_exception:
            logging.info(f"error  in creating directory at: {dir}\n error: {box_exception}")
            raise  box_exception
        
@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path,"w") as json_file:
        json.dump(data,json_file,indent=4)
        logging.info(f"saved json file at : {path}")


@ensure_annotations
def save_bin(data:object, path:Path):
    try:
        joblib.dump(data,path)
        logging.info(f"saved binary file at : {path}")
    except Exception as e:
        logging.info(f"error in saving binary file at : {path}\n error: {e}")
        raise e
