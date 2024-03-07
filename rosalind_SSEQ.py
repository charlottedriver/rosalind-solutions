# Finding a Spliced Motif
#
#
# Given: Two DNA strings s and t (each at most 1 kbp) in FASTA format
#
# Return: One collection of indices of s in which the symbols of t
# appear as a subsequences of s. If multiple solutions exisit, you
# may return any one.

def find_spliced_motif(dna_string, subsequence):
    
    instances = []
    
    dna_string = dna_string.strip().upper()
    subsequence = subsequence.strip().upper()

    if subsequence in dna_string:
        print("Subsequence found in DNA sequence")
    else:
        print("Subsequence not found in DNA sequence")
 
    for i in range(len(dna_string)):
        if dna_string[i:i+len(subsequence)] == subsequence:
            instances.append(i+1)

    index = dna_seq.find(substring_seq)

    return instances, index

from Bio import SeqIO
from Bio.Seq import Seq 

fasta_file = 'rosalind_sseq.txt'
sequences = list(SeqIO.parse(fasta_file, 'fasta'))

dna_seq = str(sequences[0].seq)
substring_seq = str(sequences[1].seq)

print(find_spliced_motif(dna_string=dna_seq, 
                         subsequence=substring_seq))
