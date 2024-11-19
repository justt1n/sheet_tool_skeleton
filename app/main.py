import codecs
import json
import logging
import os
import platform
import time
import zipfile
from datetime import datetime

import gspread
import wget

from dotenv import load_dotenv


### SETUP ###
load_dotenv('settings.env')

def setup_logging():
    # Load environment variables at the beginning of the script
    load_dotenv('settings.env')

    # Configure logging from environment variables
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_format = os.getenv('LOG_FORMAT', '%(asctime)s - %(message)s')

    # Create log file based on the current date in the logs/ directory
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}_function_calls.log")

    logging.basicConfig(filename=log_file, level=log_level, format=log_format)

### FUNCTIONS ###

### MAIN ###