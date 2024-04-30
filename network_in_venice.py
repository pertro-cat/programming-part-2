import pandas as pd
import numpy as np
from typing import List, Tuple

def read_input_data(file_path: str) -> List[Tuple[int, int, int]]:
    """
    Reads input data from a file and returns a list of edges.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    List[Tuple[int, int, int]]: A list of tuples representing the edges in the graph.
    """
    data_frame = pd.read_csv(file_path)
    matrix = data_frame.values
    edges = []
    num_vertices = len(matrix)
    for row_index in range(num_vertices):
        for column_index in range(row_index + 1, len(matrix[row_index])):
            if matrix[row_index][column_index] > 0:
                edges.append((row_index, column_index, matrix[row_index][column_index]))
    return edges

class Graph:
    """A class to represent a graph."""
    def __init__(self, size: int):
        """
        Initializes a graph with a given size.

        Parameters:
        size (int): The number of vertices in the graph.
        """
        self.root = list(range(size))
        self.rank = [1] * size
        self.edges = []

    def find_the_root_in_vertex(self, vertex: int) -> int:
        """
        Finds the root of a vertex.

        Parameters:
        vertex (int): The vertex to find the root of.

        Returns:
        int: The root of the vertex.
        """
        if self.root[vertex] != vertex:
            self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]

    def union_two_vertices(self, vertex1: int, vertex2: int) -> bool:
        """
        Unites two vertices.

        Parameters:
        vertex1 (int): The first vertex.
        vertex2 (int): The second vertex.

        Returns:
        bool: True if the vertices were united, False otherwise.
        """
        root_vertex1 = self.find(vertex1) # root is the representative of the set
        root_vertex2 = self.find(vertex2)
        if root_vertex1 != root_vertex2:
            if self.rank[root_vertex1] > self.rank[root_vertex2]:
                self.root[root_vertex2] = root_vertex1
            elif self.rank[root_vertex1] < self.rank[root_vertex2]:
                self.root[root_vertex1] = root_vertex2
            else:
                self.root[root_vertex1] = root_vertex2
                if self.rank[root_vertex1] == self.rank[root_vertex2]:
                    self.rank[root_vertex2] += 1
            return True
        return False

    def kruskal_minimum_spanning(self, num_vertices: int) -> float:
        """
        Finds the minimum spanning tree of a graph using Kruskal's algorithm.

        Parameters:
        num_vertices (int): The number of vertices in the graph.

        Returns:
        float: The weight of the minimum spanning tree, or infinity if no such tree exists.
        """
        self.edges.sort(key=lambda edge: edge[2])
        minimum_spanning_tree_weight = 0
        minimum_spanning_tree_edges = 0

        for edge_start, edge_end, weight in self.edges:
            if self.union(edge_start, edge_end):
                minimum_spanning_tree_weight += weight
                minimum_spanning_tree_edges += 1
                if minimum_spanning_tree_edges == num_vertices - 1:
                    break
        if minimum_spanning_tree_edges < num_vertices - 1:
            return float('inf')

        return minimum_spanning_tree_weight
