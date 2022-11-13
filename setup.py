import os
import sys
import shutil
from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='AstroDC',
    version='0.0.1',    
    description='A simple Python package helps us to clean data',
    url='https://github.com/mahdiabdollahii96/AstroDC',
    author='Mahdi',
    author_email='mahdiabdollahii96@gmail.com',
    license='MIT',
    packages=['AstroDC'],
    install_requires=required,
    package_data={},
    include_package_data=False,
)
