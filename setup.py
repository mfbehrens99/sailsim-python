import os
from setuptools import setup

setup(
    name='sailsim',
    version='0.1',
    description='A program to simulate sailboats',
    author='Tillman Keller & Michael Behrens',
    author_email='mfbehrens99@gmail.com',
    packages=['sailsim','sailsim\\simulation','sailsim\\world','sailsim\\algorithmus'],
    url='github.com/mfbehrens99/sailsim',
    long_description=open('README.md').read(),
)
