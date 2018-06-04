from support.find_max_value import find_max_value
from sorting_algorithms.counting_sort import counting_sort

def get_digit(n, d):
    for i in range(d-1):
        n //= 10
  
    return n % 10

def get_num_digits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1

    return i

def radix_sort(sequence):
    """Perform radix sort on a sequence of numbers."""
    max_value = find_max_value(sequence)    
    num_digits = get_num_digits(max_value)

    for digit in range(num_digits):
        sequence = counting_sort(sequence)
     
    return sequence