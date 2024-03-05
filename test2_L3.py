import unittest
import sys
sys.path.append('c:/Visual Python/lab_1/lab_2/src/')
from lab2_L3 import max_hamster


class TestMaxHamster(unittest.TestCase):
    def test_example_1(self):
        S, C = 7, 3
        hamsters = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(max_hamster(S, C, hamsters), 2, "Example 1 failed")

    def test_example_2(self):
        S, C = 19, 4
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(max_hamster(S, C, hamsters), 3, "Example 2 failed")

    def test_example_3(self):
        S, C = 2, 2
        hamsters = [[1, 50000], [1, 60000]]
        self.assertEqual(max_hamster(S, C, hamsters), 1, "Example 3 failed")

if __name__ == '__main__':
    unittest.main()
