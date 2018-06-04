def merge_sort(sequence):
    """Perform merge sort on a sequence of numbers."""
    num_entries = len(sequence)
    if num_entries > 1:
        mid = num_entries // 2
        left_half = sequence[:mid]
        right_half = sequence[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        num_left_entries = len(left_half)
        num_right_entries = len(right_half)

        left_index = 0
        right_index = 0
        total_index = 0
        while left_index < num_left_entries and right_index < num_right_entries:
            if left_half[left_index] < right_half[right_index]:
                sequence[total_index] = left_half[left_index]
                left_index = left_index + 1
            else:
                sequence[total_index] = right_half[right_index]
                right_index = right_index + 1
            total_index = total_index + 1

        while left_index < num_left_entries:
            sequence[total_index] = left_half[left_index]
            left_index = left_index + 1
            total_index = total_index + 1

        while right_index < num_right_entries:
            sequence[total_index] = right_half[right_index]
            right_index = right_index + 1
            total_index = total_index + 1
    
    return sequence
    