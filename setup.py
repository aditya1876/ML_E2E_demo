from setuptools import setup, find_packages
from typing import List

#this file is similar to pip install -r requirements.txt
#instead of the pip command you can use - python setup.py install
# It will install the packages from requirements.txt file

# why use this instead of pip install -r requirements.txt??

#Creating variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Aditya N"
DESCRIPTION="This is the first Machine Learning project for FSDS batch"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """This function is going to return the list of requriements mentioned in REQUIREMENTT_FILE_NAME.

    Returns:
        List[str]: returns the name of libraries to be installed from requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #looks for __init__.py files in all folders of the projects and installs them as packages
    install_requires=get_requirements_list()
)