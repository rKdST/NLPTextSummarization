import os
from pathlib import Path
import logging

project_name = "textSummarizer"

list_of_files = [
    #this is used for cicd deployment where the cicd related yaml file will be created
    #while commiting to the cloud, it will automatically take the code from github
    #hidden file .gitkeep is created as empty folders cannot be created
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # __init__.py is a constuctor file which is used to call local package from created like: from zz import xx
    #some other folders and files always required for any MLops project
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

#looping through the files to create the above metnioned folders
for filepath in list_of_files:
    filepath = Path(filepath) #changes the forward slash to specify the path in windows to the required format
    filedir, filename = os.path.split(filepath) #splitting the file and folder since the file needs to be created inside the folder

    #checking if the folder is empty if so the it wont replace or create the file
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #exist_ok = True will only create if the file is not present it wont overwirte
        logging.info(f"Creating directory:{filedir} for the file {filename}") #logging of execution

    #Creating the files inside the folder
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): #checking if the file exists
        with open(filepath,'w') as f: #opening the folder in write mode
            pass #since we only want to create the file
        logging.info(f"Crating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")

