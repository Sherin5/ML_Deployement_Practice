# ML_Deployement_Practice
This is my first practice using the lecture videos

This readme file includes all the commands and steps that one needs to successfully deploy the project to github and then to Heroku. This is how its done in production in the industry.

Requirements:

1.  [Github Account] (https://github.com/)
2.  [Heroku Account] (https://dashboard.heroku.com/)
3.  VS Code IDE
4.  Git cli

Step 1: Create a folder in your local machine where you want to create the project
Step 2: Create a repository on Github
Step 3: Clone in the repo in your local machine by using
```
git clone <repo link>
```
Step 4: Open the repo in VS code in your local terminal. You should see the readme, gitignore files in the VS code navigator.

Step 5: Create a virual env
```
virtualenv <env_name>
```
```
cd <env_name>
```
```
source bin/activate
```
Step 6: Create a requirements.txt file and add all the dependencies in it
Step 7: Install all the requirements from the requirements.txt file
```
pip install -r requirements.txt
```
Step 8: Create the basic app.py file and check by running
```
python app.py
```
Step 9: Make sure the venv and other files that are not required are included in the .gitignore file
Step 10: To setup a CI/CD pipeline we need the following info:
    1.  HEROKU Email
    2.  HEROKU API KEY (Can be found under account settings)
    3.  KEROKU Application Name

Step 11: Create a docker file convention : Dockerfile
Step 12: Create a .dockerignore file to ignore loading venv, .git and .gitignore files to docker
Step 13: Add the docker image
```
FROM python:3.7
```
```
COPY . /app
```
```
WORKDIR /app
```
Also add the command to run the requirements.txt file in docker
```
RUN pip install -r requirements.txt
```
Now we want to create a variable with the port
```
EXPOSE $PORT
```
Step 14: Run the flask app. Here we are binding our local IP and using the port generated in the variable. The first app in app:app is the name of the application file and the second is the name of the object in our application. Here our flask app is called app. This is the second app.
```
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
```

BUILD Docker image
```
docker build -t <image name>:<tagname> .
```
Note the image name in docker should always be in the lower case

To list docker images
```
docker images
```
To run a specific image
```
docker run -p 5001:5001 -e PORT=5001 <image id>
```

To check all the running containers run the following command
```
docker ps
```
To stop docker container
```
docker stop <container_ID>
```

Step 15: To create the CI/CD pipeline in github, we need to add the Heroku email, API key, and Heroku app name for yaml file.

We can add these details to the github repo where we are working. Navigate to Settings of the repo, then click on "Secrets" in the left pane, then click on "Actions". Add HEROKU_EMAIL, HEROKU_APP_NAME, API_KEY in the secrets of the repo.

Once the yaml file has been updated and the changes pushed to github, we can then navigate to "actions" on github repo and it should automatically start the build of  the CI/CD pileline

Step 16: Ideally, after the development of the project is done, then we need to kill the docker container. The command to kill all the containers is :
```
docker rm $(docker ps -a -q)
```
This will return all the containers that were active

Step 17: Create a setup.py file

Setp 18: Create a folder with the project name and add a __init__.py file in the folder. The __init__.py file signals that this file is a python package / module. This will enable us to import all these folder into other files.

Step 19: Once the setup file reads all the packages required for the project then it will install all the required libraries. We dont need to run pip install -r requirements.txt. Instead we use:
```
python setup.py install
```
Step 20: The packages parameter in the setup function in setup.py will look for all the __init__.py in the folder
Package is where we have __init__.py --> Folder name
python file i called as module --> File name

Step 21: Create all the child folders

Step 22: __repr__ is used when we are not using print in the function and __str__ is used when we are using inside a print function.
```
class demo:
    def __str__(self):
        return "Test123"

    def __repr__(self):
        return "test456"
```

Step 23: The components of machine learning pipeline are:
    1.  Data Ingestion -> Bring data into the system, split data into train and test
    2.  Data Validation -> Schema validation -> file name, no of columns, data type of the columns, Null check, outliers, Imblanced dataset, Perform EDA
    3.  Data transformation -> Feature engineering -> standard scaler, one hot encoding
    4.  Model training -> Model selection, hyperparameter tuning
    5.  Model Evaluation -> Test data for model evaluation, model scoring, model performance
    6.  Push model

Step 24: The data that we get from the components is pushed into Entity as artefacts. Its the same with config as well

Step 25: If you need to install the ipykernal:
```
pip install ipykernel
```

Step 26: Once we create a config variables in the entity folder, then we will use yaml file to create these variables. Config files help us save all these info in the config.yaml file.

Step 27: We created a util.py file to create helper functions. These helper functions can then be accessed from other files. 

Step 28: Initially we learnt to split the data only into train and test, however in live projects we do a split based on train, valid, and test. The model is intitally fitted on the training dataset, the hyperparameter tuning happens on the validation dataset and finally the model performance is gauged on the test dataset.

Step 29: Important step to note is that while we do a train, valid, and test split, we may apply some data transformation steps to the train and valid data. So when we add the test data, it also needs to be transformed. As such we can create a pickle model of the transformation steps. With this we can pass the test data through the pickled model for data transformation steps and also through another pickled model for the ML algo.

Step 30: We create the entity and config for the ML pipeline. These include Data ingestion, Data validation, Data transformation, Model training, Model evaluation, Push Model













