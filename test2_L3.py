import unittest
import sys
sys.path.append('c:/Visual Python/lab_1/lab_2')
from src.lab2_L3 import max_hamsters_with_sort

class TestMaxHamstersWithBinarySort(unittest.TestCase):
   
    
    def test_example1(self):
        self.assertEqual(max_hamsters_with_sort(7, 3, [[1, 2], [2, 2], [3, 1]]), 2, "Приклад 1 не пройдено")
    
    def test_example2(self):
        self.assertEqual(max_hamsters_with_sort(19, 4, [[5, 0], [2, 2], [1, 4], [5, 1]]), 3, "Приклад 2 не пройдено")
    
    def test_example3(self):
        self.assertEqual(max_hamsters_with_sort(2, 2, [[1, 50000], [1, 60000]]), 1, "Приклад 3 не пройдено")

unittest.main(argv=['first-arg-is-ignored'], exit=False)
