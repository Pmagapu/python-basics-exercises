"""
Topological Sort Algorithm
Arranges vertices of a directed acyclic graph (DAG) in linear order.
"""

from collections import deque


class TopologicalSort:
    """
    Topological Sorting Algorithms for Directed Acyclic Graphs (DAG).
    
    A topological ordering of a DAG is a linear ordering of vertices such that
    for every edge (u, v), u comes before v in the ordering.
    
    Use cases:
    - Task scheduling (with dependencies)
    - Build system dependency resolution
    - Course prerequisites
    - Instruction sequencing
    """
    
    @staticmethod
    def dfs_based(graph):
        """
        DFS-based Topological Sort.
        
        Algorithm:
        1. Perform DFS traversal from all unvisited vertices
        2. Push vertices to stack after visiting all descendants
        3. Pop from stack to get topological order
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Args:
            graph: Directed acyclic graph object
            
        Returns:
            List of vertices in topological order
            
        Raises:
            ValueError: If graph contains a cycle
        """
        if not graph.is_directed:
            raise ValueError("Topological sort is for directed graphs only")
        
        visited = set()
        rec_stack = set()  # For cycle detection
        stack = []
        
        def dfs_visit(vertex):
            """DFS helper function."""
            visited.add(vertex)
            rec_stack.add(vertex)
            
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    dfs_visit(neighbor)
                elif neighbor in rec_stack:
                    raise ValueError("Graph contains a cycle - topological sort not possible")
            
            rec_stack.remove(vertex)
            stack.append(vertex)
        
        # Visit all vertices
        for vertex in graph.vertices:
            if vertex not in visited:
                dfs_visit(vertex)
        
        # Reverse stack to get topological order
        return stack[::-1]
    
    @staticmethod
    def kahn_algorithm(graph):
        """
        Kahn's Algorithm for Topological Sort (BFS-based).
        
        Algorithm:
        1. Calculate in-degree for all vertices
        2. Add all vertices with in-degree 0 to queue
        3. Process queue: remove vertex, reduce in-degrees of neighbors
        4. Add neighbors with in-degree 0 to queue
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Args:
            graph: Directed acyclic graph object
            
        Returns:
            List of vertices in topological order
            
        Raises:
            ValueError: If graph contains a cycle
        """
        if not graph.is_directed:
            raise ValueError("Topological sort is for directed graphs only")
        
        # Calculate in-degrees
        in_degree = {v: 0 for v in graph.vertices}
        
        for vertex in graph.vertices:
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in neighbors:
                in_degree[neighbor] += 1
        
        # Queue for vertices with in-degree 0
        queue = deque([v for v in graph.vertices if in_degree[v] == 0])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            # Reduce in-degree for neighbors
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all vertices were processed (cycle detection)
        if len(result) != len(graph.vertices):
            raise ValueError("Graph contains a cycle - topological sort not possible")
        
        return result
    
    @staticmethod
    def find_longest_path(graph):
        """
        Find longest path in a DAG (useful for task scheduling).
        
        Algorithm:
        1. Topologically sort the graph
        2. Use dynamic programming to find longest path
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Args:
            graph: Directed acyclic weighted graph
            
        Returns:
            Tuple (longest_distance, path) representing the longest path
        """
        if not graph.is_directed:
            raise ValueError("Longest path algorithm is for directed graphs only")
        
        # Get topological order
        try:
            topo_order = TopologicalSort.kahn_algorithm(graph)
        except ValueError as e:
            raise ValueError(f"Cannot find longest path: {e}")
        
        # Initialize distances
        distances = {v: 0 for v in graph.vertices}
        predecessors = {v: None for v in graph.vertices}
        
        # Process vertices in topological order
        for vertex in topo_order:
            neighbors = graph.get_neighbors(vertex)
            for neighbor, weight in neighbors:
                new_distance = distances[vertex] + weight
                if new_distance > distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = vertex
        
        # Find vertex with maximum distance
        max_vertex = max(graph.vertices, key=lambda v: distances[v])
        max_distance = distances[max_vertex]
        
        # Reconstruct path
        path = []
        current = max_vertex
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        
        return max_distance, path
