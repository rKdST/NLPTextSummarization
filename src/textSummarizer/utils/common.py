#Function that are frequently used can be mentiond here
import os
from box.exceptions import BoxValueError
import yaml #since there are yaml file we need this library
from textSummarizer.logging import logger #this is the logger custom library that was created
from ensure import ensure_annotations
from box import ConfigBox #making calling value pair easier by simply using d.key insted of d["key"]
from pathlib import Path
from typing import Any

# the below mentioned method is responsible for reading any yaml files and will return all the contents inside the yaml file
@ensure_annotations #this decorator makes sure that the the veriable type within a function are of the required type and will generate an error if not
def read_yaml(path_to_yaml: Path) -> ConfigBox: #returning yaml as configbox type
    """raads yaml files and returns
    
    Arg: path_to_yaml (str): path like input
    Raises: 
        Valurerror: if yaml file is empty
        e: empty file
    Returns:
    ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

#the below mentioned method is responsible for creating the directories    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """created a list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool,optional): ignores if multiple dirs is to be created. Default is False
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# the below mentioned method is used to ger the size of the file
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path of file
        
    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"