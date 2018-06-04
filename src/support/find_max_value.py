def find_max_value(sequence):
    max_val = sequence[0]
    for number in sequence:
        if number > max_val:
            max_val = number

    return max_val
