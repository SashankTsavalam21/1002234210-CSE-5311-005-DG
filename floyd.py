from typing import List
import numpy as np

def compute_shortest_paths(weights: List[List[int]]):
    weights_matrix = np.array(weights)
    vertex_count = len(weights_matrix)
    distance_matrix = np.array([[[float(0) for _ in range(vertex_count)] for _ in range(vertex_count)] for _ in range(vertex_count)])
    distance_matrix[0] = weights_matrix

    for step in range(0, vertex_count - 1):
        next_step = step + 1
        for src in range(0, vertex_count):
            for dest in range(0, vertex_count):
                distance_matrix[next_step][src][dest] = min(
                    distance_matrix[next_step - 1][src][dest],
                    distance_matrix[next_step - 1][src][step] + distance_matrix[next_step - 1][step][dest]
                )
        print(f"\nDistance Matrix at Step {next_step}")
        print(distance_matrix[next_step])
    return distance_matrix[vertex_count - 1]

def recursive_shortest_path(weights: List[List[int]], step: int):
    vertex_count = len(weights)
    current_distances = [[float(0) for _ in range(vertex_count)] for _ in range(vertex_count)]
    current_distances = np.array(current_distances)

    for src in range(vertex_count):
        for dest in range(vertex_count):
            current_distances[src][dest] = min(weights[src][dest], weights[src][step] + weights[step][dest])

    if step == vertex_count - 1:
        return current_distances

    print(f"\nRecursive Distance Matrix at Step {step + 1}")
    print(current_distances)
    return recursive_shortest_path(current_distances, step + 1)

def build_parent_matrix(weights: List[List[int]]):
    vertex_count = len(weights)
    parent_tracker = [[float(0) for _ in range(vertex_count)] for _ in range(vertex_count)]
    parent_tracker = np.array(parent_tracker)

    for src in range(vertex_count):
        for dest in range(vertex_count):
            if src != dest and weights[src][dest] != float('inf'):
                parent_tracker[src][dest] = src
            else:
                parent_tracker[src][dest] = None

    return parent_tracker

if __name__ == "__main__":
    # Sample input graph represented as adjacency matrix
    adjacency_matrix = [
        [0, 3, 8, float('inf'), -4],
        [float('inf'), 0, float('inf'), 1, 7],
        [float('inf'), 4, 0, float('inf'), float('inf')],
        [2, float('inf'), -5, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0]
    ]

    adjacency_matrix_np = np.array(adjacency_matrix)
    print("\nIterative Floyd-Warshall Algorithm")
    print("\nFinal Matrix:\n", compute_shortest_paths(adjacency_matrix))

    print("\nRecursive Floyd-Warshall Algorithm")
    print("\nFinal Matrix:\n", recursive_shortest_path(adjacency_matrix_np, 0))

    print("\nParent Matrix:")
    print(build_parent_matrix(adjacency_matrix))
