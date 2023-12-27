#these are libraries to implement the custom logs
import os
import sys
import logging #this is a inbuilt logging module

#asctime --> is the asking time when the log is created it will save the time
#levelname --> will specify the info of level mostly information logging
#module --> where the log is created through like main.py then it will be root module
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs" # this directory will sore the logs
log_filepath = os.path.join(log_dir,"running_logs.log") #this file will be created within the directory
os.makedirs(log_dir, exist_ok=True) #will create a log directory

logging.basicConfig(
    level= logging.INFO, #will detect the information log
    format= logging_str, #logging format

    handlers=[
        logging.FileHandler(log_filepath), #this will log inside the created file
        logging.StreamHandler(sys.stdout) #this will display the log inside the terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")