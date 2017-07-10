from setuptools import setup

setup(
    name='BierePing',
    version='0.1',
    description='ca rigole',
    author=['jambon69'],
    url=['https://github.com/jambon69/biereping'],
    packages=['biereping'],
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_pymongo'
        ]
)
