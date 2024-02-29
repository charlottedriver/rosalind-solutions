# RNA Splicing
#
#
# Given: A DNA string s (of length at most 1 kbp) and a collection
# of substrings of s acting as introns. All strings are given in 
# Fasta format.
#
# Return: A protein string resulting from transcribing and translating
# the exons of s

def dna_to_rna(dna_string):
    rna = dna_string.replace('T', 'U')
    return rna

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

def rna_splicing(dna_string, introns):
    full_rna = dna_to_rna(dna_string)

    transformed_introns = [dna_to_rna(intron) for intron in introns]

    spliced_rna = full_rna
    for intron in transformed_introns:
        spliced_rna = spliced_rna.replace(intron, '')

    protein_string = rna_to_protein(spliced_rna)

    return protein_string

from Bio import SeqIO
from Bio.Seq import Seq

fasta_file = '<insert file path here>'
sequences = list(SeqIO.parse(fasta_file, 'fasta'))

dna = str(sequences[0].seq)
introns = [str(record.seq) for record in sequences[1:]]
