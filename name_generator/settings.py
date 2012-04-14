# Settings for random name generator

import os

PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])
DATA_PATH = os.path.join(PROJECT_PATH, '..', 'data',)

# NB It's a better idea to put your settings in a local_settings.py overrides file.
try:
    from local_settings import *
except ImportError:
    pass