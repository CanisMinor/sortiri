def quick_sort(sequence):
    """Perform quick sort on a sequence of numbers."""
    wall = 0
    pivot = sequence[-1]
    
    for index, num in enumerate(sequence):
        if num < pivot:
            sequence[wall], sequence[index] = sequence[index], sequence[wall]
            wall += 1
    sequence[wall], sequence[-1] = sequence[-1], sequence[wall]

    left = sequence[:wall]
    if len(left) > 0:
        left = quick_sort(left)
    right = sequence[(wall + 1):]
    if len(right) > 0:
        right = quick_sort(right)

    return left + [pivot] + right
