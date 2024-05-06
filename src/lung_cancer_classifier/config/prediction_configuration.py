import os
from lung_cancer_classifier.constants import *
from lung_cancer_classifier.utils.common import read_yaml, create_directories
from lung_cancer_classifier.entity.config_entity import PullArtifactsConfig


class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        secrets_filepath = SECRETS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.secrets = read_yaml(secrets_filepath)
        create_directories([self.config.artifacts_root])

    
    def get_pull_artifacts_config(self) -> PullArtifactsConfig:
        training = self.config.training
        
        create_directories([Path(training.root_dir)])
        
        pull_artifacts_config = PullArtifactsConfig(
            trained_model_path=Path(training.trained_model_path),
            access_key_id=self.secrets.aws.s3_ACCESS_KEY_ID,
            secret_access_key=self.secrets.aws.s3_SECRET_ACCESS_KEY,
            region=self.secrets.aws.s3_REGION,
            bucket_name=self.secrets.aws.s3_BUCKET_NAME,
            object_key_name=self.secrets.aws.s3_OBJECT_KEY_NAME
        )
        
        return pull_artifacts_config