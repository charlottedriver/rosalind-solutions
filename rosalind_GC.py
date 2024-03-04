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
    sequence_list = [str(seq_record.seq) for seq_record in sequences]
    
    id_seq_dict = {key:value for key, value in zip(id_list, sequence_list)}


    calculation = []

    for seq in id_seq_dict.values():
        gc_count = seq.count('G') + seq.count('C')
        calculation.append((gc_count/len(seq)*100))

    sorted_dict = {key:value for key, value in zip (id_list, calculation)}
    sorted_dict = sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True)
    largest_gc = sorted_dict[0]

    id = largest_gc[0].strip('\\')
    gc = largest_gc[1]

    return id, gc

from Bio import SeqIO
from Bio.Seq import Seq 

fasta_file = 'insert_filepath'
sequences = list(SeqIO.parse(fasta_file, 'fasta'))

id_value, gc_value = gc_content(sequences)

print(id_value)
print(gc_value)