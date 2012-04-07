#!/usr/bin/env python

#
# Generate (optionally) unique random names with real world probability weighting of first / last name
#
# NB, names are not guaranteed to be unique across male and female generations.
#
# Data Obtained from http://www.census.gov/genealogy/names/names_files.html
#
# Data files used:
#     data/dist.all.last
#     data/dist.female.first
#     data/dist.male.first
#
# Andrew Cutler 2012-04-07
#


import os
import sys
from random import shuffle
from optparse import OptionParser
from wc import WeightedChoice


def parse_data(file_name):

    file_path = os.path.join(os.path.split(__file__)[0], 'data', file_name)

    try:
        file = open(file_path, 'r')
    except IOError, e:
        print "%s" % e
        print "Download data files from http://www.census.gov/genealogy/names/names_files.html"
        quit()

    data = []
    for row in file:
        name = str(row[0:15]).strip()
        prob = float(row[15:20])

        data.append((name, prob))

    file.close()

    return data


def generate_names(first_wc, last_wc, number, unique_only):

    if unique_only:
        # Generate Unique Names
        d = dict()
        while len(d) < number:
            first = first_wc.next()
            last = last_wc.next()
            d['%s %s' % (first, last)] = None # This seems to be a fast way, to generate uniques using dict
        # convert to list
        names = list()
        for name in d:
            names.append(name)
        return names
    else:
        # Generate non unique names
        names = list()
        for i in range(number):
            first = first_wc.next()
            last = last_wc.next()
            names.append('%s %s' % (first, last))

    return names


def main():
    parser = OptionParser()
    parser.add_option("-u", "--unique", action="store_true", dest="unique", default=False, help="Generate unique names (within a given sex)")
    parser.add_option("-m", "--male", action="store", type="int", dest="num_male", default=0, help="Number of male names")
    parser.add_option("-f", "--female", action="store", type="int", dest="num_fem", default=0, help="Number of female names")
    (options, args) = parser.parse_args()

    if len(sys.argv) == 1:
        parser.error("No arguments")
    elif len(args) != 0:
        parser.error("Wrong number of arguments")
    else:
        # Parse data
        fem_data = parse_data('dist.female.first')
        male_data = parse_data('dist.male.first')
        last_data = parse_data('dist.all.last')

        # Create Objects
        fem_wc = WeightedChoice(fem_data);
        male_wc = WeightedChoice(male_data);
        last_wc = WeightedChoice(last_data);

        # Generate Female Names
        if options.num_fem > 0:
            output_fem = generate_names(fem_wc, last_wc, options.num_fem, options.unique)
        else:
            output_fem = []

        # Generate Male Names
        if options.num_male > 0:
            output_male = generate_names(male_wc, last_wc, options.num_male, options.unique)
        else:
            output_male = []

        # Randomly shuffle the output so male and female names are mixed
        output = output_fem + output_male
        shuffle(output)

        for name in output:
            print name


if __name__ == '__main__':
    main()