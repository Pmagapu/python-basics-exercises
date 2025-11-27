"""
Graph Data Structure
Implements both adjacency list and adjacency matrix representations.
"""


class Graph:
    """
    A flexible graph data structure supporting both directed and undirected graphs.
    Supports both weighted and unweighted edges.
    
    Attributes:
        vertices: List of all vertices in the graph
        is_directed: Boolean indicating if graph is directed
        is_weighted: Boolean indicating if graph has weighted edges
    """
    
    def __init__(self, vertices=None, is_directed=False, is_weighted=False):
        """
        Initialize a graph.
        
        Args:
            vertices: List of vertex names (optional)
            is_directed: If True, creates a directed graph
            is_weighted: If True, edges have weights
        """
        self.vertices = vertices if vertices else []
        self.vertex_count = len(self.vertices)
        self.is_directed = is_directed
        self.is_weighted = is_weighted
        
        # Adjacency list representation: {vertex: [(neighbor, weight), ...]}
        self.adj_list = {v: [] for v in self.vertices}
        
        # Adjacency matrix representation
        self.adj_matrix = None
        self._build_matrix()
    
    def _build_matrix(self):
        """Build adjacency matrix initialized with 0 or infinity for weighted graphs."""
        n = self.vertex_count
        if self.is_weighted:
            self.adj_matrix = [[float('inf')] * n for _ in range(n)]
            # Set diagonal to 0 (distance from vertex to itself)
            for i in range(n):
                self.adj_matrix[i][i] = 0
        else:
            self.adj_matrix = [[0] * n for _ in range(n)]
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.vertex_count += 1
            self.adj_list[vertex] = []
            self._build_matrix()
    
    def add_edge(self, source, destination, weight=1):
        """
        Add an edge between two vertices.
        
        Args:
            source: Source vertex
            destination: Destination vertex
            weight: Edge weight (default 1 for unweighted graphs)
        """
        if source not in self.vertices:
            self.add_vertex(source)
        if destination not in self.vertices:
            self.add_vertex(destination)
        
        # Add to adjacency list
        self.adj_list[source].append((destination, weight))
        
        # For undirected graphs, add reverse edge
        if not self.is_directed:
            self.adj_list[destination].append((source, weight))
        
        # Update adjacency matrix
        src_idx = self.vertices.index(source)
        dst_idx = self.vertices.index(destination)
        
        if self.is_weighted:
            self.adj_matrix[src_idx][dst_idx] = weight
            if not self.is_directed:
                self.adj_matrix[dst_idx][src_idx] = weight
        else:
            self.adj_matrix[src_idx][dst_idx] = 1
            if not self.is_directed:
                self.adj_matrix[dst_idx][src_idx] = 1
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex."""
        if vertex not in self.adj_list:
            raise ValueError(f"Vertex {vertex} not in graph")
        return self.adj_list[vertex]
    
    def get_edge_weight(self, source, destination):
        """Get weight of edge between two vertices."""
        for neighbor, weight in self.adj_list[source]:
            if neighbor == destination:
                return weight
        return None
    
    def __str__(self):
        """String representation of the graph."""
        result = []
        for vertex in self.vertices:
            neighbors = self.adj_list[vertex]
            if self.is_weighted:
                neighbor_str = ", ".join([f"{n}({w})" for n, w in neighbors])
            else:
                neighbor_str = ", ".join([n for n, _ in neighbors])
            result.append(f"{vertex} -> [{neighbor_str}]")
        return "\n".join(result)
