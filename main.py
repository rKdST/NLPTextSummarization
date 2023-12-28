from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage" #name of the stage
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage" #name of the stage
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx2======2x")
except:
    logger.exception(e)
    raise e

##Process
#1 lgging will be done that the stage has started
#2 the traiing pipeline will be called
#3 from the above called class the "main" method is called which will start the download file, extract.....
#4 logging the complete and lastly handeling execption 