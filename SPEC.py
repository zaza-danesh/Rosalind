#"Inferring Protein from Spectrum"

s = "CAGCATGGTATCACAGCAGAG"

#failure array of s is an array P of length n for which P[k] is the length of the longest 
#substrings s[j:k] that is equal to some prefix s[1:k-j+1]

#P = [0, 1, 1, 2, 4, 3, 6, 5 , 9 , 4 ,5 , 1]
#P[5] = 3

#substrings of s are : C, CA, CAG, CAGC, CAGCA, CAGCAT, ... 
print(s)
prefix_list = [s[0:i] for i in range(len(s)+1)]

print([len(prefix_list[i]) for i in range(len(prefix_list))])