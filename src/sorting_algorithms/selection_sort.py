def find_index_of_minimum_value(sequence):
    min_value = sequence[0]
    min_index = 0
    for index, number in enumerate(sequence):
        if number < min_value:
            min_value = number
            min_index = index
    
    return min_index

def selection_sort(sequence):
    num_values = len(sequence)
    for index in xrange(num_values):
        min_index = find_index_of_minimum_value(sequence[index:])
        sequence[index], sequence[min_index] = sequence[min_index], sequence[index]

    return sequence
