import unittest
from src.network_in_venice import Graph, read_input_data

class TestGraphMethods(unittest.TestCase):

    def test_find(self):
        graph = Graph(5)
        self.assertEqual(graph.find(0), 0)

    def test_union(self):
        graph = Graph(5)
        graph.union(0, 1)
        self.assertEqual(graph.find(0), graph.find(1))

    def test_kruskal(self):
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4)]
        graph = Graph(5)
        graph.edges = edges
        self.assertEqual(graph.kruskal(5), 10)

if __name__ == '__main__':
    unittest.main()

