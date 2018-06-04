def find_index_of_minimum_value(sequence):
    min_value = sequence[0]
    min_index = 0
    for index, number in enumerate(sequence):
        if number < min_value:
            min_value = number
            min_index = index
    
    return min_index
    
def selection_sort(sequence):
    """Perform selection sort on a sequence of numbers."""
    for fill_slot in range(len(sequence)-1,0,-1):
        position_of_max = 0
        for location in range(1,fill_slot+1):
            if sequence[location] > sequence[position_of_max]:
                position_of_max = location

        sequence[fill_slot], sequence[position_of_max] = sequence[position_of_max], sequence[fill_slot]

    return sequence