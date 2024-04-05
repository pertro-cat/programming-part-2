import unittest
import sys
sys.path.append('c:/Python/PycharmProjects/programming_part2')
from src.chess_horse import read_input, Inside, minStep, write_output

class TestChessHorse(unittest.TestCase):
    def test_read_input(self):
        N, src, dest = read_input('test_input.txt')
        self.assertEqual(N, 8)
        self.assertEqual(src, (0, 0))
        self.assertEqual(dest, (7, 7))

    def test_Inside(self):
        self.assertTrue(Inside(0, 0, 8))
        self.assertFalse(Inside(8, 8, 8))

    def test_minStep(self):
        N, src, dest = 8, (0, 0), (7, 7)
        result = minStep(src, dest, N)
        self.assertEqual(result, 6)

    def test_write_output(self):
        write_output('test_output.txt', 6)
        with open('test_output.txt', 'r') as file:
            result = int(file.read().strip())
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()