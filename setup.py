from setuptools import setup, find_packages
from typing import List

def get_requirements()->list[str]:
     
     requirements_list = list[str]=[]
     return reqirements_list

setup(
    name='sensor',
    version='0.0.1',
    author='Priyanshu',
    author_email='priyanshudwivedi435@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements()
)