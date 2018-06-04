from sorting_algorithms.insertion_sort import insertion_sort


def merge(left, right):
    """
    Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def tim_sort(sequence):
    runs = []
    sorted_runs = []
    num_entries = len(sequence)
    new_run = [sequence[0]]
    for i in range(1, num_entries):
        if i == num_entries - 1:
            new_run.append(sequence[i])
            runs.append(new_run)
            break
        if sequence[i] < sequence[i - 1]:
            if not new_run:
                runs.append([sequence[i - 1]])
                new_run.append(sequence[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(sequence[i])
    for each in runs:
        sorted_runs.append(insertion_sort(each))

    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array
