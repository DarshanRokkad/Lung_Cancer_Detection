from lung_cancer_classifier import logger
from lung_cancer_classifier.training_stages.stage_01_data_ingestion import DataIngestionTrainingPipeline
from lung_cancer_classifier.training_stages.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from lung_cancer_classifier.training_stages.stage_03_model_trainer import ModelTrainerTrainingPipeline
from lung_cancer_classifier.training_stages.stage_04_model_evaluation import ModelEvaluationTrainingPipeline


class TrainingPipeline:
    def __init__(self):
        pass
    
    
    def __ingest_data(self, STAGE_NAME):
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = DataIngestionTrainingPipeline()
            obj.initiate_data_ingestion()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e


    def __get_and_update_base_model(self, STAGE_NAME):
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = PrepareBaseModelTrainingPipeline()
            obj.initiate_prepare_base_model()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
        
        
    def __train_model(self, STAGE_NAME):
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


    def __evaluate_trained_model(self, STAGE_NAME):
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
        
    
    def initiate_training_pipeline(self):
        ''' this function will call all the components of the training pipeline '''
        try:
            logger.info(f">>>>>>>>>>>> TRAINING PIPELINE started <<<<<<<<<<<<")
            
            self.__ingest_data(STAGE_NAME="Data Ingestion stage")
            self.__get_and_update_base_model(STAGE_NAME="Prepare Base Model")
            self.__train_model(STAGE_NAME="Model Training")
            self.__evaluate_trained_model(STAGE_NAME="Model Evaluation")
            
            logger.info(f">>>>>>>>>>>> TRAINING PIPELINE completed <<<<<<<<<<<<")
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == '__main__':
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.initiate_training_pipeline()
    except Exception as e:
        logger.exception(e)
        raise e