bellman
class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

class Vertex:
    def __init__(self, label):
        self.label = label
        self.min_cost = float('inf')
        self.previous = None

def relax_edge(start, end, cost):
    if end.min_cost > start.min_cost + cost:
        end.min_cost = start.min_cost + cost
        end.previous = start

def prepare_graph(graph, source):
    for vertex in graph.vertices:
        vertex.min_cost = float('inf')
        vertex.previous = None
    source.min_cost = 0

def process_graph(graph, source):
    prepare_graph(graph, source)
    for _ in range(len(graph.vertices) - 1):
        for (start, end) in graph.edge_weights.keys():
            relax_edge(start, end, graph.edge_weights[(start, end)])
    for (start, end) in graph.edge_weights.keys():
        if end.min_cost > start.min_cost + graph.edge_weights[(start, end)]:
            return False
    return True

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {}
        self.edge_weights = {}
        for vertex in vertices:
            self.adjacency_list[vertex] = []

    def add_connection(self, start, end, cost):
        if start not in self.adjacency_list:
            self.adjacency_list[start] = [end]
        else:
            self.adjacency_list[start].append(end)
        self.edge_weights[(start, end)] = cost

    def __str__(self):
        result = "\n--- Graph Connections ---"
        for vertex in self.adjacency_list.keys():
            result += f"\n{vertex.label}: "
            for neighbor in self.adjacency_list[vertex]:
                result += f"{neighbor.label} "
        result += "\n--- End of Connections ---\n"
        return result


if __name__ == "__main__":
    # Example with custom graph data
    # A: 0, B: 1, C: 2, D: 3, E: 4

    vertices = [Vertex(i) for i in range(5)]

    edges = [Edge(vertices[0], vertices[1], 6),
             Edge(vertices[0], vertices[3], 7),
             Edge(vertices[1], vertices[2], 5),
             Edge(vertices[1], vertices[3], 8),
             Edge(vertices[1], vertices[4], -4),
             Edge(vertices[2], vertices[1], -2),
             Edge(vertices[3], vertices[2], -3),
             Edge(vertices[3], vertices[4], 9),
             Edge(vertices[4], vertices[0], 2),
             Edge(vertices[4], vertices[2], 7)]

    graph = Graph(vertices)
    for edge in edges:
        graph.add_connection(edge.start, edge.end, edge.cost)

    for connection in graph.edge_weights.keys():
        print(connection, graph.edge_weights[connection])
    print(f"Number of edges: {len(graph.edge_weights.keys())}")
    print(f"No negative cycles: {process_graph(graph, vertices[0])}")
