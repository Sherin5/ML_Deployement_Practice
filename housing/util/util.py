import yaml
from housing.exception import HousingException
import os, sys
def read_yaml_file(path:str)->dict:
    """
    Reads the content of the yaml file and returns a dictionary
    """
    try:
        with open(path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException.detailed_error_message(e, sys) from e

