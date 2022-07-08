import logging
from datetime import datetime
import os

LOG_DIR="housing_logs" #directory where logs will be stored.
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}" 
LOG_FILE_NAME=f'log_{CURRENT_TIME_STAMP}.log' #name of the log file will have timestamp
LOG_FILE_PATH=os.path.join(LOG_DIR, LOG_FILE_NAME)

#make log folder
os.makedirs(LOG_DIR, exist_ok=True) #exits_ok= True -- creates the folder if it does not exit

#config for logging
logging.basicConfig(filename=LOG_FILE_PATH,filemode='w',format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',level=logging.INFO)