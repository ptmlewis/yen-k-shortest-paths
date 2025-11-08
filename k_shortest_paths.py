import heapq
import sys

class Graph:
    def __init__(self, V: int):
        self.V = V
        self.adj = {u: [] for u in range(V)}
        self.edge_weights = {}

    def add_edge(self, u: int, v: int, w: float):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.edge_weights[(u, v)] = w
        self.edge_weights[(v, u)] = w

    def remove_edge(self, u: int, v: int):
        self.adj[u] = [(vertex, weight) for vertex, weight in self.adj[u] if vertex != v]
        self.adj[v] = [(vertex, weight) for vertex, weight in self.adj[v] if vertex != u]
        del self.edge_weights[(u, v)]
        del self.edge_weights[(v, u)]

    def dijkstra(self, src: int):
        dist = {v: float('inf') for v in range(self.V)}
        dist[src] = 0
        predecessor = {v: None for v in range(self.V)}
        pq = []
        heapq.heappush(pq, (0, src))

        while pq:
            d, u = heapq.heappop(pq)

            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    predecessor[v] = u
                    heapq.heappush(pq, (dist[v], v))

        return dist, predecessor

    def retrieve_path(self, predecessor, start, end):
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = predecessor[current]
        return path

    def has_edge(self, u, v):
        return (u, v) in self.edge_weights

    def yen_k_shortest_paths(self, start, end, K):
        distances, previous_nodes = self.dijkstra(start)
        A = [self.retrieve_path(previous_nodes, start, end)]
        A_distances = [distances[end]]

        B = []

        for k in range(1, K):
            for i in range(len(A[k - 1]) - 1):
                spur_node = A[k - 1][i]
                root_path = A[k - 1][:i + 1]

                removed_edges = {}
                for path in A:
                    if len(path) > i and root_path == path[:i + 1]:
                        edge = (path[i], path[i + 1])
                        if self.has_edge(*edge):
                            removed_edges[edge] = self.edge_weights[edge]
                            self.remove_edge(*edge)

                if spur_node != end:
                    spur_distances, spur_predecessor = self.dijkstra(spur_node)
                    spur_path = self.retrieve_path(spur_predecessor, spur_node, end)

                    if spur_path and spur_path[0] == spur_node and spur_path[-1] == end:
                        total_path = root_path[:-1] + spur_path
                        total_distance = sum(self.edge_weights[(u, v)] for u, v in zip(total_path[:-1], total_path[1:]))
                        if (total_path, total_distance) not in B:
                            heapq.heappush(B, (total_distance, total_path))

                for (u, v), weight in removed_edges.items():
                    self.add_edge(u, v, weight)

            if not B:
                break

            distance, path = heapq.heappop(B)
            A.append(path)
            A_distances.append(distance)

        return A, A_distances

def read_input(file_path):
    with open(file_path, 'r') as f_in:
        stored = [line.strip().split() for line in f_in]
    
    num_vertices = int(stored[0][0])
    num_edges = int(stored[0][1])
    edges = [(int(u), int(v), float(w)) for u, v, w in stored[1:-1]]
    source_vertex = int(stored[-1][0])
    destination_vertex = int(stored[-1][1])
    k_value = int(stored[-1][2])
    
    return num_vertices, edges, source_vertex, destination_vertex, k_value

def main():
    if len(sys.argv) != 2:
        return

    file_path = sys.argv[1]
    num_vertices, edges, source_vertex, destination_vertex, k_value = read_input(file_path)

    g = Graph(num_vertices)
    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("k =",k_value)
    k_shortest_paths, k_distances = g.yen_k_shortest_paths(source_vertex, destination_vertex, k_value)
    for idx, (path, dist) in enumerate(zip(k_shortest_paths, k_distances)):
        print(f"Distance: {dist:.2f}")

if __name__ == "__main__":
    main()