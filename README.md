# ML_E2E_demo

Demo project to showcase E2E ML.

## Steps

- [x] Create a GitHub project
- [x] Create a demo flask app

  - Create virtual env

  ```python
  python3 -m venv .venv
  source .venv/bin/activate #to activate the virtual env
  deactivate #to deactivate the env
  ```

  - Create requirements.txt file in project folder and add 'Flask' into it.
  - Install from requirements.txt file using

  ```python
  pip install -r requirements.txt
  ```

  - Create app.py file in the project folder and add code for basic flask app in it. Run the app using:

  ```python
  python app.py #if running during development
  falsk run #if running when deploying
  ```

  - Push the code to github regularly

  ```
  git add .
  git restore <filename> # to remove any file/folder from git add
  git commit -m "my commit message"
  git log #to see all the previous commits
  git status
  git remote -v #displays where the code will go on commit  and where the code will come from git pull is used.
  git push origin #pushes to your own branch name
  #create a pull request from github. Approve the chagnes and merge to main branch

  #more commands -- www.git-scm.com/docs/gittutorial
  ```

- [x] Create Docker file for the app

  - Create a new file in project folder called 'Dockerfile'
    - add the following in dockerfile
    ```
    FROM python=3.7  #gets the image from dockerhub
    COPY . /app      #copies all files(except ones mentioned in .dockerignore) into /app folder
    WORKDIR /app     #working directory is /app
    RUN pip install -r requirements.txt  #installs the packages in requirements.txt file (add gunicorn into requirements.txt)
    EXPOSE $PORT                         #env variable to specify the port the app should run on
    CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app  #launches app on localhost:$PORT
    ```
  - Create a new file in project folder called '.dockerignore'
    - add the following entries in the .dockerignore
    ```
    .venv
    .git
    .gitignore
    ```
  - Build docker image

    ```
    docker build -t <image_name>:<tagname> .

    #image_name should be lowercase
    #tagname is usually 'latest'. can be anything
    # . at the end signifies ??
    # Example - docker build -t ml-project:latest .
    ```

  - List docker images on system

  ```
  docker images
  #lists the docker images in the system.
  # note the image id from the list
  ```

  - Run Docker image

  ```
  docker run -p 5000:5000 -e PORT=5000 <image_id>
  #-p 5000:5000 specifies port
  # -e PORT=5000 is passing the environment variable PORT a value of 5000
  # image_id is the id of the image
  ```

  - Check running containers

  ```
  docker ps
  #note the container_id of the running container.
  ```

  - Stop a specific docker container

  ```
  docker stop <container_id>
  ```

- [x] Create CICD pipeline using GitHub
  - we need the following information from heroku
    - Heroku_email = <herokuemail>
    - Heroku API key = Login>click on user-icon top right>account settings>Api key section>'Reveal'>copy the key
    - heroku app name = your app name
  - Create a folder called .github
  - Create folder inside .github called workflows
  - Create main.yaml file inside workflows folder
  - Populate the yaml file and push to github
  - Set up secrets in github (variable names should exactly match the variables used in yaml file)
  - Go to Actions tab> check if any actions are running> if not you can start from here and observer the output
  - check in heroku if the app is deployed.
  - run the app and check.
- [x] Create Heroku app for deployment
  - login to heroku
  - create an app
- [ ] Create structure for ML project
- [ ] Build ML pipeline

## Process

1. Create Github project
2. Clone to local
3. Create virtual env for the project
4. Create and update setup.py file
5. Create base flask app

   - Create requirements.txt file and add package names to it

6. Create and update .gitignore file
7. Create and populate Dockerfile and .dockerignore
8. Create app folder structure:

   - Create main project folder ('housing')
   - create `__init.py__` inside this folder
   - Create folders inside main folder:
     - component
     - config
     - entity
     - exception
     - logger
     - pipeline
   - Create `__init.py` inside each sub folder

9. Update logger folder.

   - Update `__init__.py` with logging code.
   - Add the logs in .gitignore file.

10. Update exception folder

    - Update `__init__.py` with specific exception for the project.

11. Run- `python setup.py install` and verify creation of more folders and egg-info. Add them to .gitignore

12. Create Heroku app
13. Create a CICD pipeline using GitHub actions
14. Verify the app can be deployed to Heroku whenever code is pushed to github main branch
15. Create folder called 'notebook' outside the 'housing' folder
