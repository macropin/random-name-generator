#!/usr/bin/env python

from setuptools import setup
import glob

setup(name='name_generator',
    version='0.1.2',
    url='https://github.com/macropin/random-name-generator',
    packages=['name_generator',],
    scripts=['name_generator.py', 'adlibre_dms_test_data.py',],
    data_files = [ ("data", glob.glob("data/*")), ],
)
