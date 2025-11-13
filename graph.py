class Graph:
    def __init__(self):
        """
        Initialize an empty directed graph using adjacency list representation.
        The graph is generic and can work with any vertex type.
        """
        self.adjacency_list = {}  # Dictionary: vertex -> list of neighbors (outgoing edges)

    def add_vertex(self, vertex):
        """
        Add a new vertex to the graph.

        Args:
            vertex: The vertex to add (can be any data type)
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []  # Initialize empty neighbor list
            return True
        return False

    def add_edge(self, from_vertex, to_vertex):
        """
        Add a directed edge from from_vertex to to_vertex.

        Args:
            from_vertex: The starting vertex of the edge
            to_vertex: The ending vertex of the edge
        """
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            if to_vertex not in self.adjacency_list[from_vertex]:
                self.adjacency_list[from_vertex].append(to_vertex)
                return True
        return False

    def list_outgoing_adjacent_vertex(self, vertex):
        """
        List all vertices that have outgoing edges from the given vertex.

        Args:
            vertex: The vertex to check outgoing edges from

        Returns:
            list: All adjacent vertices via outgoing edges
        """
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        return []

    def remove_edge(self, from_vertex, to_vertex):
        """
        Remove a directed edge from from_vertex to to_vertex.
        """
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].remove(to_vertex)
            return True
        return False