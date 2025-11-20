import os
import sys
import logging

log_dir = "logs"
log_file_path = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s - %(message)s]",
    handlers=[logging.FileHandler(log_file_path)]
    )

logger = logging.getLogger("datascience_logger")