# Transitions and Transversions
#
#
# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
#
# Return: The transition/transversion ratio R(s1, s2).

def transitions_transversions_ratio(s1, s2):
    
    transitions_counter = 0
    transversions_counter = 0

    for i in range(len(s1)):
        
        if s1[i] == s2[i]:
            continue
        
        elif s1[i] != s2[i]:
            if s1[i] == 'A' and s2[i] == 'G':
                transitions_counter += 1
            elif s1[i] == 'G' and s2[i] == 'A':
                transitions_counter += 1
            elif s1[i] == 'C' and s2[i] =='T':
                transitions_counter += 1
            elif s1[i] == 'T' and s2[i] == 'C':
                transitions_counter += 1

            elif s1[i] == 'A' and s2[i] == 'C':
                transversions_counter += 1
            elif s1[i] == 'A' and s2[i] == 'T':
                transversions_counter += 1
            elif s1[i] == 'G' and s2[i] == 'C':
                transversions_counter += 1
            elif s1[i] == 'G' and s2[i] == 'T':
                transversions_counter += 1
            elif s1[i] == 'C' and s2[i] == 'A':
                transversions_counter += 1
            elif s1[i] == 'C' and s2[i] == 'G':
                transversions_counter += 1
            elif s1[i] == 'T' and s2[i] == 'A':
                transversions_counter += 1
            elif s1[i] == 'T' and s2[i] == 'G':
                transversions_counter += 1
            else:
                print('Error')

    ratio = transitions_counter/transversions_counter if transversions_counter != 0 else float('inf')

    return ratio