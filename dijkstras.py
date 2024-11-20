
class Edge:
    def __init__(self, origin, destination, cost):
        self.origin = origin
        self.destination = destination
        self.cost = cost

class Vertex:
    def __init__(self, value):
        self.value = value
        self.shortest_distance = float('inf')
        self.previous_vertex = None

def adjust_distance(src, dest, cost):
    if dest.shortest_distance > src.shortest_distance + cost:
        dest.shortest_distance = src.shortest_distance + cost
        dest.previous_vertex = src

def reset_single_vertex(graph, source):
    for vertex in graph.vertices:
        vertex.shortest_distance = float('inf')
        vertex.previous_vertex = None
    source.shortest_distance = 0

def get_vertex_with_minimum_distance(queue):
    min_vertex = queue[0]
    for vertex in queue:
        if vertex.shortest_distance < min_vertex.shortest_distance:
            min_vertex = vertex
    queue.remove(min_vertex)
    return min_vertex

def dijkstra_algorithm(graph, source):
    reset_single_vertex(graph, source)
    visited = []
    unvisited = graph.vertices[:]
    while unvisited:
        current_vertex = get_vertex_with_minimum_distance(unvisited)
        visited.append(current_vertex)
        for neighbor in graph.adjacency_list[current_vertex]:
            adjust_distance(current_vertex, neighbor, graph.edge_weights[(current_vertex, neighbor)])
    return visited

def get_shortest_path(vertex):
    path = []
    while vertex:
        path.append(vertex.value)
        vertex = vertex.previous_vertex
    path.reverse()
    return path

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {}
        self.edge_weights = {}
        for vertex in vertices:
            self.adjacency_list[vertex] = []

    def add_edge(self, origin, destination, cost):
        if origin not in self.adjacency_list:
            self.adjacency_list[origin] = [destination]
        else:
            self.adjacency_list[origin].append(destination)
        self.edge_weights[(origin, destination)] = cost

    def __str__(self):
        output = "\n ---Graph Connections ---"
        for vertex in self.adjacency_list.keys():
            output += f"\n{vertex.value}: "
            for neighbor in self.adjacency_list[vertex]:
                output += f"{neighbor.value} "
        output += "\n---End of Graph Connections ---\n"
        return output

if __name__ == "__main__":
    # Example from a custom graph
    # A: 0, B: 1, C: 2, D: 3, E: 4

    vertices = [Vertex(i) for i in range(5)]

    edges = [Edge(vertices[0], vertices[1], 10),
             Edge(vertices[0], vertices[3], 5),
             Edge(vertices[1], vertices[2], 1),
             Edge(vertices[1], vertices[3], 2),
             Edge(vertices[2], vertices[4], 4),
             Edge(vertices[3], vertices[1], 3),
             Edge(vertices[3], vertices[2], 9),
             Edge(vertices[3], vertices[4], 2),
             Edge(vertices[4], vertices[0], 7),
             Edge(vertices[4], vertices[2], 6)]

    graph = Graph(vertices)
    for edge in edges:
        graph.add_edge(edge.origin, edge.destination, edge.cost)

    shortest_paths = dijkstra_algorithm(graph, vertices[0])
    print("Vertex | Distance | Path")
    print("-------------------------")
    for vertex in shortest_paths:
        path = get_shortest_path(vertex)
        print(f" {vertex.value}     | {vertex.shortest_distance}       | {'->'.join(map(str, path))}")
