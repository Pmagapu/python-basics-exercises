"""
Graph Traversal Algorithms
Implements Breadth-First Search (BFS) and Depth-First Search (DFS).
"""

from collections import deque


class BFS:
    """
    Breadth-First Search (BFS) Traversal Algorithm.
    
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)
    
    Use cases:
    - Finding shortest path in unweighted graphs
    - Level-order traversal
    - Connected components
    - Bipartite graph checking
    """
    
    @staticmethod
    def traverse(graph, start_vertex):
        """
        Perform BFS traversal from a starting vertex.
        
        Args:
            graph: Graph object
            start_vertex: Starting vertex for traversal
            
        Returns:
            List of vertices in BFS order
        """
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            # Visit all neighbors
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    @staticmethod
    def shortest_path(graph, start, end):
        """
        Find shortest path between two vertices in unweighted graph.
        
        Args:
            graph: Graph object
            start: Starting vertex
            end: Ending vertex
            
        Returns:
            List representing shortest path, or None if no path exists
        """
        if start not in graph.vertices or end not in graph.vertices:
            return None
        
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        
        while queue:
            vertex, path = queue.popleft()
            
            if vertex == end:
                return path
            
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # No path found
    
    @staticmethod
    def connected_components(graph):
        """
        Find all connected components in an undirected graph.
        
        Args:
            graph: Undirected graph object
            
        Returns:
            List of connected components, where each component is a list of vertices
        """
        visited = set()
        components = []
        
        for vertex in graph.vertices:
            if vertex not in visited:
                component = []
                queue = deque([vertex])
                visited.add(vertex)
                
                while queue:
                    v = queue.popleft()
                    component.append(v)
                    
                    neighbors = graph.get_neighbors(v)
                    for neighbor, _ in neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                components.append(component)
        
        return components


class DFS:
    """
    Depth-First Search (DFS) Traversal Algorithm.
    
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for recursion stack
    
    Use cases:
    - Detecting cycles
    - Topological sorting
    - Finding strongly connected components
    - Solving maze problems
    """
    
    @staticmethod
    def traverse(graph, start_vertex):
        """
        Perform DFS traversal from a starting vertex (recursive).
        
        Args:
            graph: Graph object
            start_vertex: Starting vertex for traversal
            
        Returns:
            List of vertices in DFS order
        """
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return result
    
    @staticmethod
    def traverse_iterative(graph, start_vertex):
        """
        Perform DFS traversal from a starting vertex (iterative using stack).
        
        Args:
            graph: Graph object
            start_vertex: Starting vertex for traversal
            
        Returns:
            List of vertices in DFS order
        """
        visited = set()
        stack = [start_vertex]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                neighbors = graph.get_neighbors(vertex)
                # Add neighbors in reverse order to maintain left-to-right order
                for neighbor, _ in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    @staticmethod
    def has_cycle(graph):
        """
        Detect if graph has a cycle (works for directed graphs).
        
        Args:
            graph: Graph object
            
        Returns:
            True if cycle exists, False otherwise
        """
        visited = set()
        rec_stack = set()  # Vertices in current recursion stack
        
        def has_cycle_util(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)
            
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    if has_cycle_util(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in graph.vertices:
            if vertex not in visited:
                if has_cycle_util(vertex):
                    return True
        
        return False
