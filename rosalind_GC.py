# Computing GC Content
#
#
# Given: At most 10 DNA strings in Fasta format (of length at most 1
# kbp each).
#
# Return: The ID of the string having the highest GC-content, followed
# by the GC-content of that string. 

def gc_content(fasta_file):
    id_list = [seq_record.id for seq_record in sequences]
    sequence_list = [seq_record.seq for seq_record in sequences]
    
    id_seq_dict = {key:value for key, value in zip(id_list, sequence_list)}

    id = ''
    gc_percent = 0

    return id, gc_percent

from Bio import SeqIO
from Bio.Seq import Seq 

fasta_file = 'fasta.rtf'
sequences = list(SeqIO.parse(fasta_file, 'fasta'))
