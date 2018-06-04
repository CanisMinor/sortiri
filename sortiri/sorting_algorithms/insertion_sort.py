def insertion_sort(sequence):
    """Perform insertion sort on a sequence of numbers."""
    num_entries = len(sequence)
    outer_index =  1
    while outer_index < num_entries:
        inner_index = outer_index
        while inner_index > 0 and sequence[inner_index-1] > sequence[inner_index]:
            sequence[inner_index - 1], sequence[inner_index] = sequence[inner_index], sequence[inner_index - 1]
            inner_index = inner_index - 1

        outer_index = outer_index + 1

    return sequence
