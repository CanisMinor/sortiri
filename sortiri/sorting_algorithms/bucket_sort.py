import math
from support.find_max_value import find_max_value
from sorting_algorithms.quick_sort import quick_sort

def bucket_sort(sequence, num_buckets):
    """Perform bucket sort on a sequence of numbers."""
    max_value = find_max_value(sequence)
    bucket_width = max_value / num_buckets
    buckets = [[] for bucket_index in range(num_buckets)]
    for number in sequence:
        bucket_index = math.floor(number / bucket_width)

        # let the largest value go into the last bucket
        if bucket_index == num_buckets:
            buckets[num_buckets - 1].append(number)
        else:
            buckets[bucket_index].append(number)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(quick_sort(bucket))

    return sorted_list
