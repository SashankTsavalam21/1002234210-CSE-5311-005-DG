DFS
def depth_first_search(vertex_index, connection_matrix, visited_vertices, vertex_labels):
    print(vertex_labels[vertex_index], end=" ")
    visited_vertices[vertex_index] = 1
    
    for neighbor_index in range(len(connection_matrix)):
        if not visited_vertices[neighbor_index] and connection_matrix[vertex_index][neighbor_index] == 1:
            depth_first_search(neighbor_index, connection_matrix, visited_vertices, vertex_labels)

def main():
    MAX_VERTICES = 7
    
    connection_matrix = [
        [0, 1, 0, 0, 0, 0, 0],  
        [1, 0, 1, 1, 0, 0, 0],  
        [0, 1, 0, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0, 1, 0],  
        [0, 0, 1, 0, 0, 0, 1], 
        [0, 0, 0, 1, 0, 0, 0],  
        [0, 0, 0, 0, 1, 0, 0],  
    ]

    visited_vertices = [0] * MAX_VERTICES
    vertex_labels = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    print("DFS traversal of the graph is: ", end="")
    
    for vertex_index in range(MAX_VERTICES):
        if not visited_vertices[vertex_index]:
            depth_first_search(vertex_index, connection_matrix, visited_vertices, vertex_labels)

if __name__ == "__main__":
    main()
