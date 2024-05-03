import unittest
from src.network_in_venice import floyd_warshall_find_distance, calculate_cable_length, read_csv_file

class TestNetworkInVenice(unittest.TestCase):

    def test_floyd_warshall_find_distance(self):
        matrix = [[0, 5, float('inf'), 10],
                  [float('inf'), 0, 3, float('inf')],
                  [float('inf'), float('inf'), 0, 1],
                  [float('inf'), float('inf'), float('inf'), 0]]
        result = floyd_warshall_find_distance(matrix)
        expected = [[0, 5, 8, 9],
                    [float('inf'), 0, 3, 4],
                    [float('inf'), float('inf'), 0, 1],
                    [float('inf'), float('inf'), float('inf'), 0]]
        self.assertEqual(result, expected)

    def test_calculate_cable_length(self):
        matrix = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
        result = calculate_cable_length(matrix)
        expected = 6.0
        self.assertEqual(result, expected)

    def test_read_csv_file(self):

        result = read_csv_file('islands.csv')
        expected = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
