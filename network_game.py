import numpy as np



def ping_with_floyd_warshall(n, edges):
    inf = float('inf')
    dist = [[inf] * n for w in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for start, end, weight in edges:
        dist[start][end] = weight
        dist[end][start] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def find_optimal_server_location(num_nodes, edges, client_indices):
    distances = ping_with_floyd_warshall(num_nodes, edges)
    min_max_delay = float('inf')
    optimal_server_index = -1

    if len(client_indices) == 1:
        return 0
    if not client_indices:
        return float('inf')

    for server_index in range(num_nodes):
        if server_index not in client_indices:
            max_delay = max(distances[server_index][client] for client in client_indices)
            if max_delay < min_max_delay:
                min_max_delay = max_delay
    return min_max_delay

def main():
    with open('gamsrv.in', 'r') as file:
        n, m = map(int, file.readline().strip().split())
        clients = list(map(int, file.readline().strip().split()))
        edges = []
        for _ in range(m):
            start, end, latency = map(int, file.readline().strip().split())
            edges.append((start, end, latency))

    client_indices = [x - 1 for x in clients]  # Adjusting to zero-based index
    min_max_delay = find_optimal_server_location(n, edges, client_indices)

    with open('gamsrv.out', 'w') as file:
        file.write(f"{min_max_delay}\n")


