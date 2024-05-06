from lung_cancer_classifier.config.prediction_configuration import ConfigurationManager
from lung_cancer_classifier.components.pull_model import PullArtifacts


class DownloadArtifacts:
    def __init__(self):
        pass
    
    def download(self):        
        try:
            config = ConfigurationManager()
            pull_artifacts_config = config.get_pull_artifacts_config()
            pull_artifacts = PullArtifacts(config=pull_artifacts_config)
            pull_artifacts.download_model()
        except Exception as e:
            raise e

if __name__ == "__main__":
    download_artifacts = DownloadArtifacts()
    download_artifacts.download()