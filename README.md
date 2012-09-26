# Random Male and Female name generator

Generates random male and female names with real-world probability. (Well the occurrence of first name and last names, not the combination of the two).

Useful for generating test data for, err testing purposes.

## Install

Dev:

    pip install -e git+git@github.com:macropin/random-name-generator.git#egg=rng

Prod:

    git install git+git@github.com:macropin/random-name-generator.git

Then download the data set from http://www.census.gov/genealogy/www/data/1990surnames/names_files.html and place the three files, (dist.all.last, dist.female.first, dist.male.first) in ./data.

## Usage Examples

    ./name_generator.py -u -m 10
    ./name_generator.py -m 10 -f 10

-- Andrew Cutler
