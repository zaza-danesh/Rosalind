import numpy as np

s, s_list = [],[]
with open('rosalind_test.txt') as file:
    for line in file:
        if line.find(">") < 0:
            s.append(line.strip())
        else:
            s_list.append("".join(s))
            s = []
s_list.append("".join(s))
s_list.pop(0)

string = "ABCDABCD"
# string = "CAGCATGGTATCACAGCAGAG"
prefix_list = []
suffix_list = []
for i in range(len(string)):
	prefix_list.append(string[0:i+1])
	suffix_list.append(string[i:len(string)])

print(prefix_list)

for i in range(2):
# for i in range(len(prefix_list)-1):
	subpattern = prefix_list[i+1]
	print(subpattern)
	k = len(subpattern)
	print(k)
	print(subpattern[0:k-1])
	flag = False
	while flag == True:
		if subpattern[0:k-1] in subpattern[1:len(subpattern)-1]:
			flag = True
		else:
			k = k-1
	# while False:
	# 	subpattern[0:k-1] in subpattern
	# 	print(subpattern[0:k-1])
	# 	k=k-1

	# k = len(prefix_list)-j+1
	# print(prefix_list[j:k])

# P[1] = 0
# P[2] = 
# P = [s[j:k]]
