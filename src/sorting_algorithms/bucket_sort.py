import math
from sorting_algorithms import quick_sort

def bucket_sort(sequence, num_buckets):
    biggest = 0
    for number in sequence:
        if number > biggest:
            biggest = number

    buckets = []
    buckets.append([]) * (biggest / (num_buckets + 1))
    for number in sequence:
        bucket_index = math.floor(number / num_buckets)
        buckets[bucket_index].append(number)

    for index, bucket in enumerate(buckets):
        buckets[index] = quick_sort(bucket)

    new_list = [number for number in bucket for bucket in buckets]

    return new_list
