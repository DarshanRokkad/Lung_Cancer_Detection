from lung_cancer_classifier import logger
from lung_cancer_classifier.config.configuration import ConfigurationManager
from lung_cancer_classifier.components.model_trainer import ModelTraining


STAGE_NAME = "Model Training"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = ModelTraining(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == '__main__':
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