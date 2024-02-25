# Finding a Motif in DNA
#
#
# Given: Two DNA strings s and t (each of length at most 1 kbp)
#
# Return: All locations of t as a substring of s

def find_motif(dna_string, dna_substring):
    
    locations = []

    for i in range(len(dna_string) - len(dna_substring) + 1):
        if dna_string[i:i + len(dna_substring)] == dna_substring:
            locations.append(i+1)

    return locations