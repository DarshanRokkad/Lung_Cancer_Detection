import os
from lung_cancer_classifier.constants import *
from lung_cancer_classifier.utils.common import read_yaml, create_directories
from lung_cancer_classifier.entity.config_entity import PullArtifactsConfig


class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

    
    def get_pull_artifacts_config(self) -> PullArtifactsConfig:
        training = self.config.training
        
        create_directories([Path(training.root_dir)])
        
        pull_artifacts_config = PullArtifactsConfig(
            trained_model_path=Path(training.trained_model_path),
            access_key_id=os.environ.get('ACCESS_KEY_ID'),
            secret_access_key=os.environ.get('SECRET_ACCESS_KEY'),
            region=os.environ.get('REGION'),            
            bucket_name=os.environ.get('BUCKET_NAME'),
            object_key_name=os.environ.get('OBJECT_KEY_NAME')
        )
        
        return pull_artifacts_config