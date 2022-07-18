import yaml
from housing.exception import HousingException
import os,sys

def read_yaml_file(file_path:str)-> dict:
    """reads yaml file and returns the contents as dictionary.

    Args:
        file_path (str): path to the yaml file

    Returns:
        dict: contents of the yaml file as dictionary
    """
    try:
        with open(file_path, "r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e
