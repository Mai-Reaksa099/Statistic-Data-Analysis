import numpy as np
from modules import descriptive
x = [12,56,55]
datastr = ['apple', 'banana', 'mango', 'apple', 'mango']
mn = descriptive.mean
md = descriptive.mode(datastr)
print("mean value ",mn)
print(md)
