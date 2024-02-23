# Transcribing DNA into RNA (i.e., replace 'T' with 'U')
#
#
# Given: A DNA string t having length at most 1000 nt
#
# Return: The transcribed RNA string of t

def dna_to_rna(dna_string):
    rna = dna_string.replace('T', 'U')
    return rna