"""
Minimum Spanning Tree (MST) Algorithms
Implements Kruskal's and Prim's algorithms for finding minimum spanning trees.
"""


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure for Kruskal's algorithm.
    
    Used to efficiently detect cycles in undirected graphs.
    """
    
    def __init__(self, vertices):
        """Initialize Union-Find structure."""
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, vertex):
        """
        Find the root parent of a vertex (with path compression).
        
        Time Complexity: O(α(n)) where α is inverse Ackermann function (nearly constant)
        """
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        """
        Union two sets containing vertex1 and vertex2 (with union by rank).
        
        Returns:
            True if union was performed, False if already in same set
        """
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 == root2:
            return False
        
        # Union by rank optimization
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True


class MinimumSpanningTree:
    """
    Algorithms for finding Minimum Spanning Trees (MST).
    
    A spanning tree is a subgraph that:
    - Includes all vertices
    - Is a tree (connected and acyclic)
    - For MST, total edge weight is minimized
    """
    
    @staticmethod
    def kruskal(graph):
        """
        Kruskal's Algorithm for MST.
        
        Algorithm:
        1. Sort all edges by weight
        2. Iterate through edges in sorted order
        3. Add edge if it doesn't create a cycle (using Union-Find)
        
        Time Complexity: O(E log E) where E is number of edges
        Space Complexity: O(V)
        
        Args:
            graph: Undirected weighted graph object
            
        Returns:
            Tuple (mst_edges, total_weight) where mst_edges is list of (u, v, weight)
        """
        if graph.is_directed:
            raise ValueError("Kruskal's algorithm works only on undirected graphs")
        
        # Collect all edges with weights
        edges = []
        seen = set()
        
        for vertex in graph.vertices:
            neighbors = graph.get_neighbors(vertex)
            for neighbor, weight in neighbors:
                edge = tuple(sorted([vertex, neighbor]))
                if edge not in seen:
                    edges.append((weight, vertex, neighbor))
                    seen.add(edge)
        
        # Sort edges by weight
        edges.sort()
        
        # Build MST using Union-Find
        uf = UnionFind(graph.vertices)
        mst_edges = []
        total_weight = 0
        
        for weight, u, v in edges:
            if uf.union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                
                # MST has V-1 edges
                if len(mst_edges) == len(graph.vertices) - 1:
                    break
        
        return mst_edges, total_weight
    
    @staticmethod
    def prim(graph, start_vertex=None):
        """
        Prim's Algorithm for MST.
        
        Algorithm:
        1. Start with arbitrary vertex
        2. Maintain a set of vertices in MST
        3. Repeatedly add the minimum weight edge connecting MST to non-MST vertices
        
        Time Complexity: O(V^2) with adjacency matrix, O(E log V) with priority queue
        Space Complexity: O(V)
        
        Args:
            graph: Undirected weighted graph object
            start_vertex: Starting vertex (default: first vertex)
            
        Returns:
            Tuple (mst_edges, total_weight) where mst_edges is list of (u, v, weight)
        """
        if graph.is_directed:
            raise ValueError("Prim's algorithm works only on undirected graphs")
        
        if start_vertex is None:
            start_vertex = graph.vertices[0]
        
        if start_vertex not in graph.vertices:
            raise ValueError(f"Vertex {start_vertex} not in graph")
        
        # Track visited vertices and edges
        visited = {start_vertex}
        mst_edges = []
        total_weight = 0
        
        # All edges from visited vertices to unvisited ones
        available_edges = []
        
        # Initialize with edges from start vertex
        neighbors = graph.get_neighbors(start_vertex)
        for neighbor, weight in neighbors:
            if neighbor not in visited:
                available_edges.append((weight, start_vertex, neighbor))
        
        # Build MST
        while available_edges and len(visited) < len(graph.vertices):
            # Sort to get minimum weight edge
            available_edges.sort()
            weight, u, v = available_edges.pop(0)
            
            # Skip if both vertices already visited (cycle)
            if v in visited:
                continue
            
            # Add edge to MST
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            # Add new edges from newly visited vertex
            neighbors = graph.get_neighbors(v)
            for neighbor, w in neighbors:
                if neighbor not in visited:
                    available_edges.append((w, v, neighbor))
        
        return mst_edges, total_weight
