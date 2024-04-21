from chest_cancer_classifier.config.configuration import ConfigurationManager
from chest_cancer_classifier.components.model_trainer import ModelTraining


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