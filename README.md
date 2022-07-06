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

  ```

- [ ] Create Docker file for the app
- [ ] Create CICD pipeline using GitHub
- [ ] Create Heroku app for deployment
- [ ] Create structure for ML project
- [ ] Build ML pipeline

## Process
