# hamming distance
s1='CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT'
s2='CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'


def hamming_distance(s1, s2):

    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

print hamming_distance(s1, s2)


def hamming_distance2(s1, s2):
    diffs = 0
    for ch1,ch2 in zip(s1, s2):
        if ch1 != ch2:
            diffs += 1
    return diffs

print hamming_distance2(s1, s2)
