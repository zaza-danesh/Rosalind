import numpy as np

with open('rosalind_prob.txt') as file:
	lines = file.read().splitlines()
s = lines[0]
A = lines[1].replace(" ", ", ").split(", ")

def calc_prob(gc):
	return [gc/2, gc/2, 0.5 - gc/2, 0.5 - gc/2]

def gen_dict(p):
	list1 = ['G', 'C', 'A', 'T']
	list2 = p
	return(dict(zip(list1, list2)))

def prob_string(s, d):
	comm_log = 0
	for i in range(len(s)):
		comm_log = comm_log + np.log10(d[s[i]])
	return comm_log

for i in range(len(A)):
	p = calc_prob(float(A[i]))
	d = gen_dict(p)
	print("%.3f" % prob_string(s,d), end=" ")
print()


	