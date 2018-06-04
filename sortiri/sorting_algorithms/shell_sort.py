def shell_sort(sequence):
    """Perform shell sort on a sequence of numbers."""
    sublist_count = len(sequence) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            sequence = gap_insertion_sort(sequence, start_position, sublist_count)

        sublist_count = sublist_count // 2

    return sequence

def gap_insertion_sort(sequence, start, gap):
    """Perform gap insertion sort on a sequence of numbers."""
    for index in range(start + gap, len(sequence), gap):
        current_value = sequence[index]
        position = index

        while position >= gap and sequence[position-gap] > current_value:
            sequence[position] = sequence[position-gap]
            position = position-gap

        sequence[position] = current_value

    return sequence
