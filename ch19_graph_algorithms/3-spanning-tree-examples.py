"""
3-spanning-tree-examples.py
Understanding Minimum Spanning Trees (MST)

This file demonstrates:
- Kruskal's Algorithm for MST
- Prim's Algorithm for MST
- Applications of spanning trees
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ch19_graph_algorithms.lib.graph import Graph
from ch19_graph_algorithms.lib.tree import MinimumSpanningTree


def example_1_kruskal_algorithm():
    """Demonstrate Kruskal's Algorithm."""
    print("=" * 60)
    print("Example 1: Kruskal's Algorithm for MST")
    print("=" * 60)
    
    # Create a weighted undirected graph
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E'], is_directed=False, is_weighted=True)
    
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for source, dest, weight in edges:
        graph.add_edge(source, dest, weight)
    
    print("\nOriginal Graph:")
    print(graph)
    print(f"\nTotal edges in graph: {len(edges)}")
    print(f"Edges with weights: {edges}")
    
    mst_edges, total_weight = MinimumSpanningTree.kruskal(graph)
    
    print("\nMinimum Spanning Tree (Kruskal's):")
    for u, v, w in mst_edges:
        print(f"  {u} - {v} : {w}")
    print(f"\nTotal weight of MST: {total_weight}")
    print(f"Number of edges in MST: {len(mst_edges)}")


def example_2_prim_algorithm():
    """Demonstrate Prim's Algorithm."""
    print("\n" + "=" * 60)
    print("Example 2: Prim's Algorithm for MST")
    print("=" * 60)
    
    # Create the same graph as Kruskal example
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E'], is_directed=False, is_weighted=True)
    
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for source, dest, weight in edges:
        graph.add_edge(source, dest, weight)
    
    print("\nOriginal Graph:")
    print(graph)
    
    mst_edges, total_weight = MinimumSpanningTree.prim(graph, start_vertex='A')
    
    print("\nMinimum Spanning Tree (Prim's starting from A):")
    for u, v, w in mst_edges:
        print(f"  {u} - {v} : {w}")
    print(f"\nTotal weight of MST: {total_weight}")
    print(f"Number of edges in MST: {len(mst_edges)}")


def example_3_network_design():
    """Real-world example: Network design."""
    print("\n" + "=" * 60)
    print("Example 3: Network Design (Real-world Application)")
    print("=" * 60)
    
    # Design fiber optic network connecting cities (minimize cable length)
    graph = Graph(vertices=['Seattle', 'Portland', 'San Francisco', 
                           'Los Angeles', 'Denver'], 
                 is_directed=False, is_weighted=True)
    
    connections = [
        ('Seattle', 'Portland', 174),
        ('Portland', 'San Francisco', 635),
        ('San Francisco', 'Los Angeles', 383),
        ('Seattle', 'Denver', 1315),
        ('Portland', 'Denver', 1332),
        ('Los Angeles', 'Denver', 1015)
    ]
    
    for source, dest, distance in connections:
        graph.add_edge(source, dest, distance)
    
    print("\nAvailable connections with distances (miles):")
    for source, dest, distance in connections:
        print(f"  {source:15} - {dest:15} : {distance} miles")
    
    mst_edges, total_distance = MinimumSpanningTree.kruskal(graph)
    
    print("\nOptimal Network (Minimum Total Cable):")
    for source, dest, distance in mst_edges:
        print(f"  {source:15} - {dest:15} : {distance} miles")
    print(f"\nTotal cable needed: {total_distance} miles")


def example_4_road_network():
    """Real-world example: Road network."""
    print("\n" + "=" * 60)
    print("Example 4: Road Network (Real-world Application)")
    print("=" * 60)
    
    # Design road network connecting towns (minimize total road length)
    graph = Graph(vertices=['Town A', 'Town B', 'Town C', 'Town D', 'Town E'],
                 is_directed=False, is_weighted=True)
    
    roads = [
        ('Town A', 'Town B', 5),
        ('Town A', 'Town C', 2),
        ('Town B', 'Town C', 3),
        ('Town B', 'Town D', 7),
        ('Town C', 'Town D', 1),
        ('Town D', 'Town E', 2),
        ('Town C', 'Town E', 4)
    ]
    
    for source, dest, length in roads:
        graph.add_edge(source, dest, length)
    
    print("\nAvailable roads with lengths:")
    for source, dest, length in roads:
        print(f"  {source:10} - {dest:10} : {length} units")
    
    mst_edges, total_length = MinimumSpanningTree.prim(graph, start_vertex='Town A')
    
    print("\nOptimal Road Network:")
    for source, dest, length in mst_edges:
        print(f"  {source:10} - {dest:10} : {length} units")
    print(f"\nTotal road length needed: {total_length} units")


def example_5_algorithm_comparison():
    """Compare Kruskal's and Prim's on same graph."""
    print("\n" + "=" * 60)
    print("Example 5: Kruskal vs Prim Comparison")
    print("=" * 60)
    
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E', 'F'],
                 is_directed=False, is_weighted=True)
    
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 3),
        ('C', 'E', 6),
        ('D', 'E', 7),
        ('D', 'F', 1),
        ('E', 'F', 2)
    ]
    
    for source, dest, weight in edges:
        graph.add_edge(source, dest, weight)
    
    print("\nGraph with 6 vertices and 9 edges")
    
    kruskal_mst, kruskal_weight = MinimumSpanningTree.kruskal(graph)
    prim_mst, prim_weight = MinimumSpanningTree.prim(graph, start_vertex='A')
    
    print(f"\nKruskal's MST (weight: {kruskal_weight}):")
    for u, v, w in sorted(kruskal_mst):
        print(f"  {u} - {v} : {w}")
    
    print(f"\nPrim's MST (weight: {prim_weight}):")
    for u, v, w in sorted(prim_mst):
        print(f"  {u} - {v} : {w}")
    
    print("\nBoth algorithms produce MST with the same total weight!")
    print(f"Verified: {kruskal_weight == prim_weight}")


if __name__ == "__main__":
    example_1_kruskal_algorithm()
    example_2_prim_algorithm()
    example_3_network_design()
    example_4_road_network()
    example_5_algorithm_comparison()
    
    print("\n" + "=" * 60)
    print("Spanning Tree Examples Complete!")
    print("=" * 60)
