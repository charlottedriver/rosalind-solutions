# Translating RNA into Protein
#
#
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp)
#
# Return: The protein string encoded by s

def rna_to_protein(rna_string):
    
    amino_acic_dict = {'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAU':'N', 'AAC':'N',
    'GAU':'D', 'GAC':'D',
    'UGU':'C', 'UGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAU':'H', 'CAC':'H',
    'AUU':'I', 'AUC':'I', 'AUA':'I',
    'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'AAA':'K', 'AAG':'K',
    'AUG':'M',
    'UUU':'F', 'UUC':'F',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'UGG':'W',
    'UAU':'Y', 'UAC':'Y',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V'}

    protein_string = ''

    for i in range(0, len(rna_string), 3):
        codon = rna_string[i:i+3]
        if codon in amino_acic_dict:
            amino_acid = amino_acic_dict[codon]
            if amino_acid == '*':
                break
            protein_string += amino_acid
    
    return protein_string