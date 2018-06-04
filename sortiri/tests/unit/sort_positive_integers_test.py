
import unittest
import nose.tools as nt  # contains testing tools like ok_, eq_, etc.
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.bucket_sort import bucket_sort
from sorting_algorithms.counting_sort import counting_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.insertion_sort import insertion_sort
from ..sorting_algorithms.merge_sort import merge_sort
from ..sorting_algorithms.quick_sort import quick_sort
from ..sorting_algorithms.radix_sort import radix_sort
from ..sorting_algorithms.selection_sort import selection_sort
from ..sorting_algorithms.shell_sort import shell_sort
from ..sorting_algorithms.tim_sort import tim_sort
 
class PositiveIntegersTest(unittest.TestCase):
    """ Test sorting algorithms on an array of positive integers. """

    def setUp(self):
        self.input_array = [6, 2, 1, 7, 8, 3, 5, 9, 4, 12, 8, 5, 32, 8, 5, 2, 6, 9, 34, 21, 7]
        self.expected = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 12, 21, 32, 34]

    def tearDown(self):
         print("Positive integers tests finished.")
     
    def bubble_sort_test(self):
        actual = bubble_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())

    def bucket_sort_test(self):
        actual = bubble_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def counting_sort_test(self):
        actual = counting_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def heap_sort_test(self):
        actual = heap_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def insertion_sort_test(self):
        actual = insertion_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def merge_sort_test(self):
        actual = merge_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def quick_sort_test(self):
        actual = quick_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def radix_sort_test(self):
        actual = radix_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def selection_sort_test(self):
        actual = selection_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())

    def shell_sort_test(self):
        actual = shell_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())        

    def tim_sort_test(self):
        actual = tim_sort(self.input_array)
        self.assertTrue((actual == self.expected).all())
