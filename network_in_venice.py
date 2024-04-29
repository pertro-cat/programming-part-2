import pandas as pd
import numpy as np


def read_input_data(file_path):
    data_frame = pd.read_csv(file_path)
    matrix = data_frame.values

    edges = []
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, len(matrix[i])):
            if matrix[i][j] > 0:
                edges.append((i, j, matrix[i][j]))
    return edges

class Graph:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
        self.edges = []

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
            return True
        return False

    def kruskal(self, num_vertices):
        self.edges.sort(key=lambda x: x[2])
        mst_weight = 0
        mst_edges = 0

        for u, v, weight in self.edges:
            if self.union(u, v):
                mst_weight += weight
                mst_edges += 1
                if mst_edges == num_vertices - 1:
                    break

        if mst_edges < num_vertices - 1:
            return float('inf')

        return mst_weight

def write_output_data(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))

def start(file_path):
    edges = read_input_data(file_path)
    graph = Graph(len(edges))
    graph.edges = edges
    result = graph.kruskal(len(edges))
    write_output_data('lengh_cable.csv', result)



