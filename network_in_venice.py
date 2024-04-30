import csv
import numpy as np

def floyd_warshall_find_distance(matrix):
    """
    The function uses the Floyd-Warshall algorithm to find the shortest
     paths between all pairs of vertices in a graph.

    Parameters:
    matrix (list of list of int): Distance matrix, where matrix[i][j]
    corresponds to the distance between vertices i and j.

    Returns:
    matrix (list of list of int): Updated distance matrix after executing
    the Floyd-Warshall algorithm.
    """
    num_vertices = len(matrix)
    for intermediate_vertex in range(num_vertices):
        for start_vertex in range(num_vertices):
            for end_vertex in range(num_vertices):
                matrix[start_vertex][end_vertex] = min(matrix[start_vertex][end_vertex],
                   matrix[start_vertex][intermediate_vertex] + matrix[intermediate_vertex][end_vertex])
    return matrix


def calculate_cable_length(matrix):
    """
    The function calculates the total length of the cable needed to cover
     all distances in the matrix.

    Parameters:
    matrix (list of list of int): Distance matrix, where matrix[i][j]
    corresponds to the distance between vertices i and j.

    Returns:
    total_length (float): Total length of the cable.
    """
    total_length = 0
    for row in matrix:
        total_length += sum(row)
    return total_length / 2


def read_csv_file(file_name):
    """
    The function reads a CSV file and converts it into a matrix.

    Parameters:
    file_name (str): Name of the CSV file.

    Returns:
    matrix (list of list of int): Matrix obtained from the CSV file.
    """
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        matrix = list(reader)
    matrix = [[int(value) for value in row] for row in matrix]
    return matrix



