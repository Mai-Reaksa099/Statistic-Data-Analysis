import numpy as np
from collections import Counter
import statistics
def mean(x):
    val = sum(x)/len(x)
    return val;
def medain(x1):
    n = len(x1)
    index = n //2
    if n % 2:
        return sorted(x1)[index]
    return sum(sorted(x1)[index - 1: index + 1])/2
def mode(x):
    y = {}
    for a in x:
        if not a in y:
            y[a] = 1
        else:
            y[a] += 1
    return [g for g,l in y.items() if l == max(y.values())]
