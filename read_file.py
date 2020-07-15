import numpy as np
from numpy import array as arr

s = []
s_list = []

with open('rosalind_test.txt') as file:
    for line in file:
        if line.find(">") < 0:
            s.append(line.strip())
        else:
            s_list.append("".join(s))
            s = []
s_list.append("".join(s))
s_list.pop(0)

