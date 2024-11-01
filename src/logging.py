import logging
import os
from datetime import datetime   #date  time is required for checking which time our log render 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #this string format time mon/date/year/hour/min/sec

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  #get current working directory check whether LOG_FILE if not in directory then create this folder and logs into it 

os.makedirs(logs_path, exist_ok=True)   # exist_ok=True--> if that particular path is exists then log add what are file we are having into that same log file inside that folder  

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)