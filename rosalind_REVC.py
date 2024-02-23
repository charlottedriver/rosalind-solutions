# Complementing a Strand of DNA
#
#
# Given: A DNA string s of length at most 1000 bp
#
# Return: The reverse complement of s

def reverse_complement(dna_string):

    # Step 1: Replace each Nucleotide with its Complement
    complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement_sequence = ''.join(complement_dict[nucleotide] for nucleotide in dna_string)

    # Step 2: Reverse the Sequence
    reverse_complement_sequence = complement_sequence[::-1]

    return reverse_complement_sequence