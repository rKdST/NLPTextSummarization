import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

#this is similar to DataIngestion created in the first notebook
#it will take the output from the above code block and will be initialised within "self.config"
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config #will be initialized here

    def validate_all_files_exist(self)-> bool: #method to validate file existance
        try:
            validate_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES: #will check if the files are available
                    validate_status=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status: {validate_status}")
                
                else:
                    validate_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation status: {validate_status}")     

            return validate_status #these files will be saved inside data_validation folder

        except Exception as e:
            raise e