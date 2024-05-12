from collections import defaultdict
from typing import List, Tuple


def read_input(filename: str) -> Tuple[int, int, List[str]]:
    """
    Reads the input file and returns the width, height and grid.

    Parameters:
    filename (str): The name of the input file.

    Returns:
    Tuple[int, int, List[str]]: A tuple containing the width, height and grid.
    """
    with open(filename, 'r') as fin:
        W, H = map(int, fin.readline().strip().split())
        grid = [fin.readline().strip() for _ in range(H)]
    return W, H, grid


def indiana_jones_rectangular_walk(W: int, H: int, grid: List[str]) -> int:
    """
    Calculates the total number of paths in the grid.

    Parameters:
    W (int): The width of the grid.
    H (int): The height of the grid.
    grid (List[str]): The grid.

    Returns:
    int: The total number of paths.
    """
    num_paths_to_cell = [[0] * W for _ in range(H)]
    for row in range(H):
        num_paths_to_cell[row][0] = 1

    for col in range(1, W):
        cumulative_sum = defaultdict(int)
        for row in range(H):
            cumulative_sum[grid[row][col]] += num_paths_to_cell[row][col - 1]
        for row in range(H):
            num_paths_to_cell[row][col] = cumulative_sum[grid[row][col]]

    total_paths = sum(num_paths_to_cell[row][W - 1] for row in range(H))
    return total_paths


def count_paths(filename_input='ijones.in', filename_output='ijones.out'):
    """
    Reads the input file, calculates the total number of paths and writes the result to the output file.

    Parameters:
    filename_input (str): The name of the input file.
    filename_output (str): The name of the output file.
    """
    W, H, grid = read_input(filename_input)
    total_paths = indiana_jones_rectangular_walk(W, H, grid)
    with open(filename_output, 'w') as fout:
        fout.write(str(total_paths) + '\n')








