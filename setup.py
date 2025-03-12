#!/usr/bin/env python3

from setuptools import setup

# This setup script is for a Python package named 'glit'. It specifies the package version, the packages to include, and defines a console script entry point for the command-line interface.
from setuptools import setup
setup(name='glit',
      version='1.0',
      packages=['glit'],
      entry_points={
          'console_scripts': [
              'glit = glit.cli:main'
          ]
      })