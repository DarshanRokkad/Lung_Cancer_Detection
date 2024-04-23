<h1 align="center">Chest Cancer🫁 Classification 🤖</h1>

---

<h3 align="center">Problem Statement</h3>

Given an image we have to classify wheather the image is Adeno carinoma cancer or not.

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

<h3 align="center">Project Structure</h3>

```
│  
├── .dvc                                      <-- used for data and pipeline versioning
│  
├── .github
│   │
│   └── workflow                          
│       │
│       └── main.yml                         <-- contains yml code to create CI-CD pipeline for github actions
│  
├── artificats                               <-- contains data and trained models(in remote repository)
│  
├── images                                   <-- contains images used in readme file
│  
├── config                                   <-- contains yaml file where we mention the configuration of our project
│  
├── notebooks                                <-- contains jupyter notebook where experiments and research work is done
│
├── src
│   │
│   ├── components
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── data_ingestion.py             <-- module which reads data from different data source and do train test split
│   │   │                                        then save raw data, train data and test data inside artifact folder 
│   │   │
│   │   ├── data_transformation.py        <-- module which takes training and test dataset and then do feature engineering
│   │   │                                        then save preprocessor as pickle file inside artifact folder 
│   │   │
│   │   ├── model_training.py             <-- module which takes preprocessed training and test data and 
│   │   │                                        this data is used to train different models and selects best model 
│   │   │                                        it also perform hyperparameter tuning 
│   │   │
│   │   │
│   │   └── model_evaluation.py           <-- module which calculate the performance metrics
│   │
│   ├── pipeline
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── training_pipeline.py          <-- module used to train the model using training components
│   │   │
│   │   └── prediction_pipeline.py        <-- module takes the input data given by user through flask web application and returns the prediction
│   │
│   ├── __init__.py
│   │
│   ├── exception.py                         <-- module to display the custom exception
│   │
│   ├── logger.py                            <-- module to create log folder for each execution and log the events whenever required.
│   │
│   └── utils.py                             <-- module to which contians functions that are commonly used.
│
├── .dvcignore                               <-- similar to .gitignore 
│
├── .gitignore                               <-- used to ignore the unwanted file and folders
│
├── LICENSE                                  <-- copyright license for the github repository 
│
├── README.md                                <-- used to display the information about the project
│
├── app.py                                   <-- this is contains web page written in streamlit
│
├── dvc.lock                                 <-- this is file is output of pipeline versioning
│
├── dvc.yaml                                 <-- this is yaml file contains code to reproduce training pipeline
│
├── params.yaml                              <-- this yaml file contains the parameters and values used during model training
│
├── requirements.txt                         <-- text file which contain the dependencies/packages used in project 
│
├── scores.json                              <-- contains the score recorded after model training
│
├── setup.py                                 <-- python script used for building python packages of the project
│
└── template.py                              <-- program used to create the project structure
```

---