from chest_cancer_classifier.config.configuration import ConfigurationManager
from chest_cancer_classifier.components.model_evaluation import ModelEvaluation


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = ModelEvaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()