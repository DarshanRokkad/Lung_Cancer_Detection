import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

package_name = 'lung_cancer_classifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    
    "setup.py",
    "requirements.txt",
    "notebook/experiments.ipynb",
    
    "src/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/config/configuration.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/training_stages/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")