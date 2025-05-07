from collections import deque

class UndirectedGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def adjacent_vertices(self, key):
        return list(self.edges.get(key, []))

    def bfs(self, start_key):
        visited = set()
        queue = deque()
        result = []
        queue.append(self.vertices[start_key])
        visited.add(self.vertices[start_key])
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for adjacent_vertex in self.edges[vertex]:
                if not adjacent_vertex in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

        return result

    def clear(self):
        self.vertices.clear()
        self.edges.clear()

    def delete_edge(self, u, v):
        self.edges[u].discard(v)
        self.edges[v].discard(u)

    def delete_vertex(self, key):
        for edge in self.edges[key]:
            self.edges[edge].discard(key)

        del self.edges[key]
        del self.vertices[key]

    def dfs(self, start_key):
        visited = set()
        result = []

        def _dfs(vertex):
            visited.add(vertex)
            result.append(vertex)
            for adjacent_vertex in self.edges[vertex]:
                if adjacent_vertex not in visited:
                    _dfs(adjacent_vertex)

        _dfs(self.vertices[start_key])

        return result

    def insert_edge(self, u, v):
        self.edges[u].add(v)
        self.edges[v].add(u)

    def insert_vertex(self, key):
        self.vertices[key] = key
        self.edges[key] = set()

    def is_empty(self):
        return not self.vertices