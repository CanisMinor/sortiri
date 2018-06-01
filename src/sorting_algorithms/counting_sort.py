import warnings

def find_maximum_value(sequence):
    max_val = sequence[0]
    for number in sequence:
        if number > max_val:
            max_val = number

    return max_val

def counting_sort(sequence):
    '''
        Statement:
           Given a disordered list of repeated integers, rearrange the
           integers in natural order.
    '''
    num_entries = len(sequence)
    max_val = find_maximum_value(sequence)
    num_buckets = max_val + 1
    counts = [0] * num_buckets

    for a in sequence:
        if a >= 0 and a < num_buckets and isinstance(a, int):
            counts[a] += 1
        else:
            warnings.warn("A value that was either non-positive or non-integer was detected in the sequence. \
                           This value has been ignored in the counting sort routine.")
            

    seq_index = 0
    for integer_value in xrange(num_buckets):
        for count in xrange(counts[integer_value]):
            sequence[seq_index] = integer_value
            seq_index += 1

    return sequence