#!/usr/bin/env python

#
# Script which generates test data for Adlibre DMS scalability testing
#
# https://redmine.adlibre.net/issues/701
#

import os
import random
from random import shuffle

from name_generator import parse_data, generate_names
from name_generator.wc import WeightedChoice
from name_generator.settings import DATA_PATH


# Config
NUM_FEM=1
NUM_MALE=1

DOCS_MIN=1
DOCS_MAX=2

DOC_PREFIX='ADL-'

def main():

    file_path = lambda x: os.path.join(DATA_PATH, x)
    fem_data = parse_data(file_path('dist.female.first'))
    male_data = parse_data(file_path('dist.male.first'))
    last_data = parse_data(file_path('dist.all.last'))

    # Create Objects
    fem_wc = WeightedChoice(fem_data);
    male_wc = WeightedChoice(male_data);
    last_wc = WeightedChoice(last_data);

    # Generate Female Names
    output_fem = generate_names(fem_wc, last_wc, NUM_FEM, False)

    # Generate Male Names
    output_male = generate_names(male_wc, last_wc, NUM_MALE, False)

    output = output_fem + output_male

    # Generate a result containing: employee_id, employee name, document
    employee_id = 0
    doc_id = 0
    result = []
    for employee in output:
        employee_id = employee_id + 1
        for doc in range(0, random.randint(DOCS_MIN, DOCS_MAX)):
            doc_id = doc_id + 1
            result.append((employee_id, employee, '%s%s' % (DOC_PREFIX, doc_id)))

    # Randomly shuffle the output
    shuffle(result)

    print result



if __name__ == '__main__':
    main()
