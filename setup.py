#!/usr/bin/env python3

from setuptools import setup

setup (name = 'glit',
      version = '1.0',
      packages = ['glit'],
      entry_points = {
          'console_scripts' : [
              'glit = glit.cli:main'
          ]
      })