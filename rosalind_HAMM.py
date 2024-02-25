# Counting Point Mutations
#
#
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp)
#
# Return The Hamming distance

def point_mutation_counter(s, t):
    
    counter = 0

    for i in range(len(s)):
        if s[i] == t[i]:
            counter += 0
        elif s[i] != t[i]:
            counter += 1
    
    return counter
