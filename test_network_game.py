import unittest
import sys
import tempfile
from src.network_game import main, gamsrv_in, gamsrv_out
import os

sys.path.append('c:/Python/PycharmProjects/programming_part2')
from src.network_game import ping_with_floyd_warshall, find_optimal_server_location



class TestNetworkGame(unittest.TestCase):
    def test_all_nodes_are_clients(self):
        num_nodes = 5
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)]
        client_indices = [0, 1, 2, 3, 4]
        result = find_optimal_server_location(num_nodes, edges, client_indices)
        self.assertEqual(result, float('inf'))

    def test_all_nodes_are_servers(self):
        num_nodes = 5
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)]
        client_indices = []
        result = find_optimal_server_location(num_nodes, edges, client_indices)
        self.assertEqual(result, float('inf'))

    def test_one_client_and_server(self):
        num_nodes = 2
        edges = [(0, 1, 1)]
        client_indices = [0]
        result = find_optimal_server_location(num_nodes, edges, client_indices)
        self.assertEqual(result, 0)

    def test_one_client_or_server(self):
        num_nodes = 1
        edges = []
        client_indices = [0]
        result = find_optimal_server_location(num_nodes, edges, client_indices)
        self.assertEqual(result, 0)

    def test_no_clients_or_servers(self):
        num_nodes = 5
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)]
        client_indices = []
        result = find_optimal_server_location(num_nodes, edges, client_indices)
        self.assertEqual(result, float('inf'))

    def test_read_write_file_error_handling(self):
        with self.assertRaises(IOError):
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                temp.write(b'6 6\n1 2 6\n1 3 10\n3 4 80\n4 5 50\n5 6 20\n2 3 40\n2 4 100\n')
                temp_name = temp.name

            old_input_name = 'gamsrv.in'
            old_output_name = 'gamsrv.out'
            new_input_name = temp_name
            new_output_name = '/non/existent/path'

            try:
                network_game.gamsrv_in = new_input_name
                network_game.gamsrv_out = new_output_name

                main()

            finally:
                os.remove(new_input_name)
                network_game.gamsrv_in = old_input_name
                network_game.gamsrv_out = old_output_name




if __name__ == '__main__':
    unittest.main()