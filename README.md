<h1 align="center">🫁 Lung Cancer Detection 🔍</h1>

---

<h3 align="center">Problem Statement</h3>

Given a CT Scan image we have to classify wheather the CT Scan image is Adenocarinoma cancer or not.

---

<h3 align="center">Solution Explaination</h3>

Click the below image to see vedio solution explaination. 

[![YouTube Video](images/youtube-tumbnail.png)](https://www.youtube.com/embed/______)

---

<h3 align="center">Approch for the problem</h3>

<h4 align="center">Workflows</h4>

1. Update config.yaml
2. Update secrets.yaml (Optional)
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the stages
8. Update the Training pipeline
9. Update the dvc.yaml

``` Note : When we use mlflow before runing code we have to set the mlflow variables ```
``` Note : When we do pipeline versioning we have to have driver code in each stages itself ```

---

<h3 align="center">Project UI</h3>

<p align="center"><img src="images/project-ui.png" width="700" height="400"></p>

---

<h3 align="center">Integration of DVC</h3>

<p align="center">I have used DVC for versioning of training pipeline.</p>
<p align="center"><img src="images/dvc1.png" width="700" height="400"></p>

---

<h3 align="center">Integration of Mlflow and Dags</h3>

<p align="center">I used mlflow to manage my deep learning life cycle by logging the evalution metrics and plots.</p>
<p align="center">I used dagshub as a remote repository with mlflow to store the logs and artifacts.</p>
<p align="center"><img src="images/mlflow1.png" width="700" height="400"></p>

---

<h3 align="center">Deployment of streamlit application on AWS cloud</h3>

<p align="center">I have used AWS ECR and AWS EC2 to deploy our application.</p>
<p align="center"><img src="images/deploy1.png" width="700" height="400"></p>

---

<h3 align="center">Project Structure</h3>

```
│  
├── .dvc                                               <-- used for data and pipeline versioning
│  
├── .github/workflow                                   <-- contains yml code to create CI-CD pipeline for github actions 
│          
├── artificats (remote)                                <-- contains dataset and trained models(in remote repository)
│          
├── config                                             <-- contains yaml file where we mention the configuration of our project
│          
├── images                                             <-- contains images used in readme file
│          
├── logs (remote)                                      <-- contains logs created during running of pipelines and components
│          
├── notebook                                           <-- contains jupyter notebook where experiments and research work is done
│  
├── secrets (remote)                                   <-- contains a yaml file which contains the api tokens, secreat keys, password and many more
│
├── src
│    │
│    └── lung_cancer_classifier (package)
│          │
│          ├── components
│          │     │
│          │     ├── __init__.py
│          │     │
│          │     ├── data_ingestion.py                 <-- this module downloads zip file dataset present in google drive and extracts zip file in local machine
│          │     │
│          │     ├── prepare_base_model.py             <-- this module pulls the vgg-16 base model and adds custom layers at the end then saves custom model
│          │     │
│          │     ├── model_trainer.py                  <-- this module take the custom model and train it with the training data and validates with validation data
│          │     │
│          │     └── model_evaluation.py               <-- this module test the trained model with the testing data and log the evaluation metrics and artifacts to dagshub using mlflow 
│          │
│          ├── config                                  <-- this folder contains module that have the configuration manager which is used to manage configuration of each components of training pipeline  
│          │
│          ├── constants                               <-- module contains path of the yaml file 
│          │
│          ├── entity                                  <-- has a python file which contains data class of each component of the training pipeline
│          │
│          ├── pipeline
│          │     │
│          │     ├── __init__.py
│          │     │
│          │     ├── training_pipeline.py              <-- module used to train the model in different stages
│          │     │
│          │     └── prediction_pipeline.py            <-- module takes the image from user through web application and returns the prediction
│          │
│          ├── training_stages                         <-- folder used to create stages by using the configuration manager and components 
│          │     │
│          │     ├── __init__.py
│          │     │
│          │     ├── stage_01_data_ingestion.py        <-- module used to create a data ingestion configuration object and then ingest data into local machine
│          │     │
│          │     ├── stage_02_prepare_base_model.py    <-- module used to create custom model by using vgg-16 as base model and modify/add few fully connected layers at last
│          │     │
│          │     ├── stage_03_model_trainer.py         <-- module used to train custom model using training and validation data
│          │     │
│          │     └── stage_04_model_evaluation.py      <-- module used to evaluate the trained model using test data
│          │
│          ├── utils                                   <-- module to which contians functions that are commonly used.
│          │
│          └── __init__.py                             <-- this python file contains logger
│          
├── .dvcignore                                         <-- similar to .gitignore 
│          
├── .gitignore                                         <-- used to ignore the unwanted file and folders
│          
├── LICENSE                                            <-- copyright license for the github repository 
│          
├── README.md                                          <-- used to display the information about the project
│          
├── app.py                                             <-- this is contains web page written in streamlit
│          
├── dvc.lock                                           <-- this is file is output of pipeline versioning
│          
├── dvc.yaml                                           <-- this is yaml file contains code to reproduce training pipeline
│          
├── params.yaml                                        <-- this yaml file contains the parameters and values used during model training
│          
├── requirements.txt                                   <-- text file which contain the dependencies/packages used in project 
│          
├── scores.json                                        <-- contains the score recorded after model evaluation
│          
├── setup.py                                           <-- python script used for building our project as a python packages
│          
└── template.py                                        <-- program used to create the project structure
```

---