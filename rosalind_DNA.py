# Counting DNA Nucleotides
#
#
# Given: A DNA string of length at most 1000 nt
#
# Return: Four integers (separated by spaces) counting the 
# respective number of times that the symbols 'A', 'C', 'G' 
# and 'T' occur in s

def nucleotide_counter(dna_string):
    A = 0
    C = 0
    G = 0
    T = 0

    for nucleotide in dna_string:
        if nucleotide == 'A':
            A += 1
        elif nucleotide == 'C':
            C += 1
        elif nucleotide == 'G':
            G += 1
        elif nucleotide == 'T':
            T += 1
    
    print(str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))