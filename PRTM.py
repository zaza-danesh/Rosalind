
#"Calculating Protein Mass"
weight = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}


file = open('rosalind_prtm.txt', 'r')
aa = file.read()

#aa = "SKADYEK"
mass=0

for i in aa.strip():
	mass +=  weight[i]
print(mass)

#with water, list compression
print("%.2f"%(sum([ weight[i] for i in aa.strip() ])+18.01528))



#-----------------------------------------------------
##read in mass table to string
#f = open('mass_table.txt', 'r')
#mass_tbl = f.read()
##mass string to list
#mass_tbl = mass.split()
##mass string to dict
#mass_tbl = dict(zip(mass[0::2],mass[1::2]))

#-------------------------------------------------------