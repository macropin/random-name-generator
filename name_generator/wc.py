# Origin of the method below somewhat dubious. Believed to be in the public domain. - AC
# http://gamedev.stackexchange.com/questions/20881/handling-random-with-unique-chance-in-python
# http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/
# http://stackoverflow.com/questions/4113307/pythonic-way-to-select-list-elements-with-different-probability

import random
import bisect

# Returns a random value, considering the weights of each item.
class WeightedChoice(object):
    def __init__(self, weights):
        self.totals = []
        self.weights = weights
        running_total = 0

        for w in weights:
            running_total += w[1]
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        i = bisect.bisect_right(self.totals, rnd)
        return self.weights[i][0]