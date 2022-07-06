# ML_E2E_demo

Demo project to showcase E2E ML.

## Steps

- [x] Create a GitHub project
- [ ] Create a demo flask app

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

- [ ] Create Docker file for the app

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
    #tagname is usually 'latest'
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

- [ ] Create CICD pipeline using GitHub
  - we need the following information from heroku
    - Heroku_email = <herokuemail>
    - Heroku API key = Login>click on user-icon top right>account settings>Api key section>'Reveal'>copy the key
    - heroku app name = your app name
- [ ] Create Heroku app for deployment
  - login to heroku
  -
- [ ] Create structure for ML project
- [ ] Build ML pipeline

## Process
