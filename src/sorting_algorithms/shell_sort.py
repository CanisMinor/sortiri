def shell_sort(sequence):
    sublist_count = len(sequence) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
           gap_insertion_sort(sequence, start_position, sublist_count)
           
        sublist_count = sublist_count // 2

def gap_insertion_sort(sequence, start, gap):
    for index in range(start + gap, len(sequence), gap):
        current_value = sequence[index]
        position = index

        while position >= gap and sequence[position-gap] > current_value:
            sequence[position] = sequence[position-gap]
            position = position-gap

        sequence[position] = current_value