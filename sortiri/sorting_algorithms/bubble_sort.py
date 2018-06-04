def bubble_sort(sequence):
    """Perform bubble sort on a sequence of numbers."""
    num_entries = len(sequence)
    for stop_index in reversed(range(num_entries)):
        for index in range(stop_index):
            if sequence[index] > sequence[index + 1]:
                sequence[index], sequence[index + 1] = sequence[index + 1], sequence[index]
    
    return sequence