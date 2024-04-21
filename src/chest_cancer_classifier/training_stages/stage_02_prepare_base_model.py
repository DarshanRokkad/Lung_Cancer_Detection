from chest_cancer_classifier.config.configuration import ConfigurationManager
from chest_cancer_classifier.components.prepare_base_model import PrepareBaseModel


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    
    def initiate_prepare_base_model(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()