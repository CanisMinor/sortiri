def bubble_sort(sequence):
    num_entries = len(sequence)
    for stop_index in reversed(xrange(num_entries - 1)):
        for index in xrange(stop_index):
            if sequence[index] > sequence[index + 1]:
                sequence[index], sequence[index + 1] = sequence[index + 1], sequence[index]
    
    return sequence