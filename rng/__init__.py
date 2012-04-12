

def parse_data(file_path):

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
