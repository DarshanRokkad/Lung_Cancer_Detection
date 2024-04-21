from chest_cancer_classifier import logger
from chest_cancer_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chest_cancer_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chest_cancer_classifier.pipeline.stage_03_model_trainer import ModelTrainerTrainingPipeline
from chest_cancer_classifier.pipeline.stage_04_model_evaluation import ModelEvaluationTrainingPipeline


# For testing purpose 

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.initiate_prepare_base_model()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info(f"*******************")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info(f"*******************")
except Exception as e:
    logger.exception(e)
    raise e