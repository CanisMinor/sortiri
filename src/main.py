from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.bucket_sort import bucket_sort
from sorting_algorithms.counting_sort import counting_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.radix_sort import radix_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.shell_sort import shell_sort
from sorting_algorithms.tim_sort import tim_sort
from sorting_algorithms.tree_sort import tree_sort

arr = [6, 2, 1, 7, 8, 3, 5, 9, 4, 12, 8, 5, 32, 8, 5, 2, 6, 9, 34, 21, 7]
no_repeats_array = [7, 6, 1, 4, 2, 3, 9, 8, 5]
ans = tree_sort(no_repeats_array)
print("Sorted array is %s" % ("".join(str(ans))))
