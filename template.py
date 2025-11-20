import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

project_name = "datascience_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config.yaml",
    "app.py",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "templates/index.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    fildir,filname = os.path.split(filepath)

    if fildir != "":
        os.makedirs(fildir,exist_ok=True)
        logging.info(f"creating dir for {fildir}")

    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") :
            # creating empty file
            pass
        logging.info(f"The dir exists and creating empty file {filepath}")

    else:
        logging.info(f"The file already exists: {filepath}")
    