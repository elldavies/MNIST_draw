import logging 
import os 
from datetime import datetime

# create a logger file name and log path 
LOG_FILE=f"{datetime.now().strftime('%d-%m-%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True) # append files if it exsits 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# create a logger object for INFO
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)