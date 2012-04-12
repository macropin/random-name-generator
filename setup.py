#!/usr/bin/env python

from distutils.core import setup
import glob

setup(name='rng',
    version='0.1',
    url='https://github.com/macropin/random-name-generator',
    packages=['rng',],
    scripts=['name_generator.py',],
    data_files = [ ("data", glob.glob("data/*")), ],
)