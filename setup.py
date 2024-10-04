from setuptools import find_packages,setup
from typing import List

ignore_e = '-e .'


def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]
        if ignore_e in requirements:
            requirements.remove(ignore_e)
        return requirements

setup(
    name = 'DiamondPricePrediction',
    version = '0.0.1',
    author = 'AnkitSinghGusain',
    author_email = 'ankitjguain@gmail.com',
    install_requires = get_requirements('requirement.txt'),
    packages = find_packages()
)