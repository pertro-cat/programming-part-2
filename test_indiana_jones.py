import unittest
from collections import defaultdict
from typing import List, Tuple
from src.indiana_jones import read_input, indiana_jones_rectangular_walk, count_paths

class TestIndianaJones(unittest.TestCase):
    def test_read_input(self):
        test_input = 'test_ijones.in'
        with open(test_input, 'w') as f:
            f.write('3 3\nabc\nbca\ncab\n')

        expected_output = (3, 3, ['abc', 'bca', 'cab'])
        self.assertEqual(read_input(test_input), expected_output)

    def test_indiana_jones_rectangular_walk_basic(self):
        W, H = 3, 3
        grid = ['abc', 'bca', 'cab']
        expected_output = 3
        self.assertEqual(indiana_jones_rectangular_walk(W, H, grid), expected_output)

    def test_indiana_jones_rectangular_walk_jumps(self):
        W, H = 3, 3
        grid = ['aaa', 'bab', 'cac']
        expected_output = 9
        self.assertEqual(indiana_jones_rectangular_walk(W, H, grid), expected_output)

    def test_indiana_jones_rectangular_walk_single_row(self):
        W, H = 5, 1
        grid = ['abcde']
        expected_output = 1
        self.assertEqual(indiana_jones_rectangular_walk(W, H, grid), expected_output)

    def test_indiana_jones_rectangular_walk_single_column(self):
        W, H = 1, 5
        grid = ['a', 'b', 'c', 'd', 'e']
        expected_output = 5
        self.assertEqual(indiana_jones_rectangular_walk(W, H, grid), expected_output)

    def test_indiana_jones_rectangular_walk_large_grid(self):
        W, H = 2000, 2
        grid = ['a' * W, 'b' * W]
        expected_output = 2
        self.assertEqual(indiana_jones_rectangular_walk(W, H, grid), expected_output)

    def test_count_paths(self):
        test_input = 'test_ijones.in'
        test_output = 'test_ijones.out'

        with open(test_input, 'w') as f:
            f.write('3 3\nabc\nbca\ncab\n')

        count_paths(test_input, test_output)

        with open(test_output, 'r') as f:
            result = int(f.readline().strip())

        expected_output = 3
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
