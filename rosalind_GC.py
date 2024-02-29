# Computing GC Content
#
#
# Given: At most 10 DNA strings in Fasta format (of length at most 1
# kbp each).
#
# Return: The ID of the string having the highest GC-content, followed
# by the GC-content of that string. 

def gc_content(fasta_file):
    id = ''
    gc = 0
    return id, gc

from Bio import SeqIO
from Bio.Seq import Seq 
