"""
2-traversal-examples.py
Understanding Graph Traversal: BFS and DFS

This file demonstrates:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Finding shortest paths
- Detecting cycles
- Connected components
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ch19_graph_algorithms.lib.graph import Graph
from ch19_graph_algorithms.lib.traversal import BFS, DFS


def example_1_bfs_traversal():
    """Demonstrate BFS traversal."""
    print("=" * 60)
    print("Example 1: Breadth-First Search (BFS) Traversal")
    print("=" * 60)
    
    # Create graph
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E', 'F'], is_directed=False)
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
    
    for source, dest in edges:
        graph.add_edge(source, dest)
    
    print("\nGraph Structure:")
    print(graph)
    
    print("\nBFS Traversal starting from 'A':")
    bfs_order = BFS.traverse(graph, 'A')
    print(f"Order: {' -> '.join(bfs_order)}")
    print("(Visits vertices level by level)")


def example_2_dfs_traversal():
    """Demonstrate DFS traversal."""
    print("\n" + "=" * 60)
    print("Example 2: Depth-First Search (DFS) Traversal")
    print("=" * 60)
    
    # Create the same graph as BFS example
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E', 'F'], is_directed=False)
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
    
    for source, dest in edges:
        graph.add_edge(source, dest)
    
    print("\nGraph Structure:")
    print(graph)
    
    print("\nDFS Traversal starting from 'A' (Recursive):")
    dfs_order = DFS.traverse(graph, 'A')
    print(f"Order: {' -> '.join(dfs_order)}")
    print("(Explores as deep as possible before backtracking)")
    
    print("\nDFS Traversal starting from 'A' (Iterative):")
    dfs_order_iter = DFS.traverse_iterative(graph, 'A')
    print(f"Order: {' -> '.join(dfs_order_iter)}")


def example_3_shortest_path():
    """Find shortest path using BFS."""
    print("\n" + "=" * 60)
    print("Example 3: Finding Shortest Path (BFS)")
    print("=" * 60)
    
    # Create graph
    graph = Graph(vertices=['Home', 'Office', 'Gym', 'Store', 'Park', 'Library'],
                  is_directed=False)
    edges = [
        ('Home', 'Office'),
        ('Home', 'Gym'),
        ('Office', 'Store'),
        ('Gym', 'Park'),
        ('Store', 'Library'),
        ('Park', 'Library')
    ]
    
    for source, dest in edges:
        graph.add_edge(source, dest)
    
    print("\nLocation Network:")
    print(graph)
    
    start, end = 'Home', 'Library'
    path = BFS.shortest_path(graph, start, end)
    
    if path:
        print(f"\nShortest path from '{start}' to '{end}':")
        print(f"  {' -> '.join(path)}")
        print(f"  Distance: {len(path) - 1} steps")
    else:
        print(f"No path found from '{start}' to '{end}'")


def example_4_connected_components():
    """Find connected components in a graph."""
    print("\n" + "=" * 60)
    print("Example 4: Finding Connected Components (BFS)")
    print("=" * 60)
    
    # Create graph with disconnected components
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E', 'F', 'G'], is_directed=False)
    edges = [
        ('A', 'B'),
        ('B', 'C'),
        ('D', 'E'),
        ('E', 'F'),
        ('F', 'D'),
        ('G', 'G')  # Self-loop
    ]
    
    for source, dest in edges:
        graph.add_edge(source, dest)
    
    print("\nGraph with Disconnected Components:")
    print(graph)
    
    components = BFS.connected_components(graph)
    print(f"\nNumber of connected components: {len(components)}")
    for i, component in enumerate(components, 1):
        print(f"  Component {i}: {component}")


def example_5_cycle_detection():
    """Detect cycles using DFS."""
    print("\n" + "=" * 60)
    print("Example 5: Cycle Detection (DFS)")
    print("=" * 60)
    
    # Graph without cycle
    print("\nGraph 1 (No cycle - Tree structure):")
    graph1 = Graph(vertices=['A', 'B', 'C', 'D'], is_directed=True)
    edges1 = [('A', 'B'), ('A', 'C'), ('B', 'D')]
    
    for source, dest in edges1:
        graph1.add_edge(source, dest)
    
    print(graph1)
    has_cycle1 = DFS.has_cycle(graph1)
    print(f"Has cycle: {has_cycle1}")
    
    # Graph with cycle
    print("\nGraph 2 (With cycle):")
    graph2 = Graph(vertices=['A', 'B', 'C', 'D'], is_directed=True)
    edges2 = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')]  # D->B creates cycle
    
    for source, dest in edges2:
        graph2.add_edge(source, dest)
    
    print(graph2)
    has_cycle2 = DFS.has_cycle(graph2)
    print(f"Has cycle: {has_cycle2}")


def example_6_comparison():
    """Compare BFS vs DFS on the same graph."""
    print("\n" + "=" * 60)
    print("Example 6: BFS vs DFS Comparison")
    print("=" * 60)
    
    graph = Graph(vertices=['1', '2', '3', '4', '5', '6', '7'],
                  is_directed=False)
    edges = [
        ('1', '2'), ('1', '3'),
        ('2', '4'), ('2', '5'),
        ('3', '6'), ('3', '7')
    ]
    
    for source, dest in edges:
        graph.add_edge(source, dest)
    
    print("\nGraph Structure (Tree):")
    print(graph)
    
    bfs_result = BFS.traverse(graph, '1')
    dfs_result = DFS.traverse(graph, '1')
    
    print(f"\nBFS traversal:  {' -> '.join(bfs_result)}")
    print(f"DFS traversal:  {' -> '.join(dfs_result)}")
    print("\nBFS explores level-by-level (breadth)")
    print("DFS explores depth-first (depth)")


if __name__ == "__main__":
    example_1_bfs_traversal()
    example_2_dfs_traversal()
    example_3_shortest_path()
    example_4_connected_components()
    example_5_cycle_detection()
    example_6_comparison()
    
    print("\n" + "=" * 60)
    print("Graph Traversal Examples Complete!")
    print("=" * 60)
