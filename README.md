# Random Male and Female name generator

Generates random male and female names with real-world probability. (Well the occurrence of first name and last names, not the combination of the two).

Useful for generating test data for, err testing purposes.

## Install

Dev:

    pip install -e git+https://github.com/macropin/random-name-generator.git#egg=name_generator

Prod:

    pip install git+https://github.com/macropin/random-name-generator.git

Then download the data set from [www2.census.gov/topics/genealogy/1990surnames/](https://www2.census.gov/topics/genealogy/1990surnames/) and place the three files, (`dist.all.last`, `dist.female.first`, `dist.male.first`) in ./data.

## Usage Examples

    ./name_generator.py -u -m 10
    ./name_generator.py -m 10 -f 10

-- Andrew Cutler
