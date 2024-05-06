import boto3
from lung_cancer_classifier.entity.config_entity import PullArtifactsConfig


class PullArtifacts:
    def __init__(self, config: PullArtifactsConfig):
        self.config = config
        
    def download_model(self):

        s3_resource = boto3.resource(
            service_name='s3',
            region_name=self.config.region,
            aws_access_key_id=self.config.access_key_id,
            aws_secret_access_key=self.config.secret_access_key
        )

        s3_resource.Bucket(self.config.bucket_name).download_file(Key=self.config.object_key_name, Filename=self.config.trained_model_path)