#"Consensus and Profile"
import numpy as np

cns_dict={0: "A", 1: "C", 2:"G", 3:"T"}
def split(word): 
    return [char for char in word]

s = []
s_list = []

with open('rosalind_cons.txt') as file:
    for line in file:
        if line.find(">") < 0:
            s.append(line.strip())
        else:
            s_list.append("".join(s))
            s = []
s_list.append("".join(s))
s_list.pop(0)
# print(s_list)
# print(len(s_list))

s_matrix = []
# a,c,g,t= [],[],[],[]
for i in range(len(s_list)):
	s_matrix.append(split(s_list[i]))

s_array = np.array(s_matrix)
s_arrayT = s_array.T
s_matrix = s_arrayT.tolist()

acgt = np.arange(4*len(s_matrix))
c=-1
for l in ["A", "C", "G", "T"]:
	c +=1
	for i in range(len(s_matrix)):
		acgt[c*len(s_matrix) + i] = "".join(s_matrix[i]).count(l)
	
acgt_matrix = acgt.reshape(4,len(s_matrix)) 

# print(np.argmax(acgt_matrix, axis=0))
indices = np.argmax(acgt_matrix, axis=0)

output = ["*"]*len(s_matrix)

for i in range(len(s_matrix)):
	output[i] =  cns_dict[indices[i]]

print("%s" % "".join(output))
for i in range(len(cns_dict)):
	print(cns_dict[i]+ ": ", end="")
	print(*acgt_matrix[i,:])