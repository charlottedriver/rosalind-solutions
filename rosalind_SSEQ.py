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

    return instances

from Bio import SeqIO
from Bio.Seq import Seq 

fasta_file = 'practice.txt'
sequences = list(SeqIO.parse(fasta_file, 'fasta'))

dna_seq = str(sequences[0].seq)
substring_seq = str(sequences[1].seq)
