from textSummarizer.constants import * #since we want to access all the constants
from textSummarizer.utils.common import read_yaml, create_directories #these files have already created inside common src/utils/common
from textSummarizer.entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) #this is a dictionary pair call only possible because of ConfigBox

    #this code block reads the constants using the function we have desigend within common.py present inside utils 
    #(eg: procedure to read the yaml file)
    # it also saves the file inside the artifacts folder

    

    def get_data_ingestion_config(self) -> DataIngestionConfig: # the return type is set to DataIngesionConfig which has been stated above in code block 1
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config