from collections import deque

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        N = int(lines[0].strip().split(', ')[0])
        src = tuple(map(int, lines[1].strip().split(', ')))
        dest = tuple(map(int, lines[2].strip().split(', ')))
    return N, src, dest
class ChessHorse:
    def __init__(self, row=0, col=0, distance=0):
        self.row = row
        self.col = col
        self.distance = distance

def Inside(row, col, N):
    if row >= 0 and row < N and col >= 0 and col < N:
        return True
    return False


def minStep(horsepos, targetpos, N):
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    queue = []
    queue.append(ChessHorse(horsepos[0], horsepos[1], 0))
    visited = [[False for i in range(N + 1)] for j in range(N + 1)]
    visited[horsepos[0]][horsepos[1]] = True

    while len(queue) > 0:
        t = queue[0]
        queue.pop(0)

        if t.row == targetpos[0] and t.col == targetpos[1]:
            return t.distance

        for i in range(8):
            x = t.row + row[i]
            y = t.col + col[i]

            if Inside(x, y, N) and not visited[x][y]:
                visited[x][y] = True
                queue.append(ChessHorse(x, y, t.distance + 1))
                return -1



def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

def main():
    filename = 'input.txt'
    N, src, dest = read_input(filename)
    moves = minStep(src, dest, N)
    write_output('output.txt', moves)

if __name__ == "__main__":
    main()
