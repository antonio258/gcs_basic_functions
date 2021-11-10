import os
from setuptools import setup

requirements = f'{os.path.dirname(os.path.realpath(__file__))}/requirements.txt'

if os.path.isfile(requirements):
    with open(requirements) as f:
        install_requires = f.read().splitlines()

setup(
    name='gcs',
    version='1.0',
    packages=['gcs_basic'],
    url='',
    license='',
    author='antonio',
    author_email='antonio258p@gmail.com',
    description='Gcp simple functions',
    install_requires=install_requires
)
