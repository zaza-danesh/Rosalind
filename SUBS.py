#"Finding a Motif in DNA"

# s = "GATATATGCATATACTT"
# t = "ATAT"

file_list = open("rosalind_subs.txt").readlines()
s = file_list[0].strip()
t = file_list[1].strip()
# print(s)
# print(t)

pos_list = []

for i in range(len(s)):
    if t in s[i:i+len(t)]:
        pos_list.append(i+1)
        print(pos_list[-1], end =" ")
print("")