codon = {"UUU": "F", "CUU": "L",  "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG":"S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "CAA": "Q", "AAA": "K", "GAA": "E", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "CGA": "R", "AGA": "R", "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G", "UAA": "Stop", "UAG": "Stop", "UGA": "Stop"}
codon_list = ["UUU", "CUU",  "AUU", "GUU", "UUC", "CUC", "AUC", "GUC", "UUA", "CUA", "AUA", "GUA", "UUG", "CUG", "AUG", "GUG", "UCU", "CCU", "ACU", "GCU", "UCC", "CCC", "ACC", "GCC", "UCA", "CCA", "ACA", "GCA", "UCG", "CCG", "ACG", "GCG", "UAU", "CAU", "AAU", "GAU", "UAC", "CAC", "AAC", "GAC", "CAA", "AAA", "GAA", "CAG", "AAG", "GAG", "UGU", "CGU", "AGU", "GGU", "UGC", "CGC", "AGC", "GGC", "CGA", "AGA", "GGA", "UGG", "CGG", "AGG", "GGG", "UAA", "UAG", "UGA"]

# for i in codon_list:
# 	print(dict[i])

rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

file = open('rosalind_prot.txt', 'r')
rna = file.read()

protein_string = ""

# for i in range(0, len(rna), 3):
for i in range(0, len(rna)-(3+len(rna)%3), 3):
    if codon[rna[i:i+3]] == "Stop" :
        break
    protein_string += codon[rna[i:i+3]]

print(protein_string)
