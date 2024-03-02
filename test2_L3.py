import unittest
import sys
sys.path.append('c:/Visual Python/lab_1/lab_2')
from lab2_L3 import max_hamster


class TestMaxHamster(unittest.TestCase):
    def test_example1(self):
        S = 7
        C = 3
        hamsters = [[1, 2], [2, 2], [3, 1]]
        result = max_hamster(S, C, hamsters)
        self.assertEqual(result, 2)

    def test_example2(self):
        S = 19
        C = 4
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        result = max_hamster(S, C, hamsters)
        self.assertEqual(result, 3)

    def test_example3(self):
        S = 2
        C = 2
        hamsters = [[1, 50000], [1, 60000]]
        result = max_hamster(S, C, hamsters)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()