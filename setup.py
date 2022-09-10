from setuptools import setup, find_packages
from typing import List
def get_requirement_list()->List[str]:
    """
    Return a list of all the packages required for the project
    """
    with open("requirements.txt") as packages:
        return packages.readlines()

## Declaring variables for setup
Project_name = "HOUSING PREDICTOR"
VERSION= "0.0.1"
AUTHOR= "SHERIN"
DESCRIPTION="This is a regression problem for predicting house prices"
PACKAGES = ["housing"]
setup(
    name=Project_name,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirement_list()

)
