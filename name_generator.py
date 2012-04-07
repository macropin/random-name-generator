#!/usr/bin/env python

#
# Generate a unique random names with real world probability weighting of first / lastname
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


def main():
    parser = OptionParser()
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

        # Generate Unique Female Names
        output_fem = dict()
        while len(output_fem) < options.num_fem:
            first = fem_wc.next()
            last = last_wc.next()
            output_fem['%s %s' % (first, last)] = None # This seems to be a fast way, to generate uniques using dict

        # Generate Unique Male Names
        output_male = dict()
        while len(output_male) < options.num_male:
            first = male_wc.next()
            last = last_wc.next()
            output_male['%s %s' % (first, last)] = None

        for name in output_fem:
            print name

        for name in output_male:
            print name


if __name__ == '__main__':
    main()