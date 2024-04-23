from lung_cancer_classifier import logger
from lung_cancer_classifier.config.configuration import ConfigurationManager
from lung_cancer_classifier.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = 'Prepare Base Model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    
    def initiate_prepare_base_model(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.create_custom_model()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.initiate_prepare_base_model()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
        logger.info(f"*******************")
    except Exception as e:
        logger.exception(e)
        raise e