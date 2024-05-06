from lung_cancer_classifier.constants import *
from lung_cancer_classifier.utils.common import read_yaml, create_directories
from lung_cancer_classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig, EvaluationConfig, PullArtifactsConfig


class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        secrets_file_path = SECRETS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.secrets = read_yaml(secrets_file_path)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        ''' returns own custom data type '''
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config


    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
    
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training.training_data),
            validation_data=Path(training.validation_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
        
    
    def get_evaluation_config(self) -> EvaluationConfig:
        mlflow_secrets = self.secrets.mlflow
        params = self.params
        
        eval_config = EvaluationConfig(
            path_of_model=Path(self.config.training.trained_model_path),
            testing_data=Path(self.config.evaluation.testing_data),
            mlflow_uri=mlflow_secrets.MLFLOW_TRACKING_URI,
            all_params=params,
            params_image_size=params.IMAGE_SIZE,
            params_batch_size=params.BATCH_SIZE
        )
        
        return eval_config