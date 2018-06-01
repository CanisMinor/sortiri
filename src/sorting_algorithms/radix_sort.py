from sorting_algorithms import counting_sort

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

def radix_sort(sequence, max_value):
    num_digits = get_num_digits(max_value)

    for digit in range(num_digits):
        sequence = counting_sort(sequence, max_value, lambda a: get_digit(a, digit + 1))
     
    return sequence