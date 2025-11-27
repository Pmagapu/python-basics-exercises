"""
1-graph-basics.py
Understanding Graph Fundamentals and Creating Graphs

This file demonstrates:
- Creating undirected and directed graphs
- Adding vertices and edges
- Different graph representations (adjacency list vs matrix)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ch19_graph_algorithms.lib.graph import Graph


def example_1_undirected_graph():
    """Create and explore an undirected graph."""
    print("=" * 60)
    print("Example 1: Undirected Graph (Social Network)")
    print("=" * 60)
    
    # Create an undirected graph
    graph = Graph(
        vertices=['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        is_directed=False,
        is_weighted=False
    )
    
    # Add edges (friendships)
    edges = [
        ('Alice', 'Bob'),
        ('Alice', 'Charlie'),
        ('Bob', 'Diana'),
        ('Charlie', 'Diana'),
        ('Diana', 'Eve')
    ]
    
    for source, destination in edges:
        graph.add_edge(source, destination)
    
    print("\nFriendship Network:")
    print(graph)
    print(f"\nAlice's friends: {[n for n, _ in graph.get_neighbors('Alice')]}")
    print(f"Total connections: {len(edges)}")


def example_2_directed_graph():
    """Create and explore a directed graph."""
    print("\n" + "=" * 60)
    print("Example 2: Directed Graph (Web Pages)")
    print("=" * 60)
    
    # Create a directed graph
    graph = Graph(
        vertices=['Home', 'About', 'Products', 'Contact', 'Blog'],
        is_directed=True,
        is_weighted=False
    )
    
    # Add directed edges (hyperlinks)
    edges = [
        ('Home', 'About'),
        ('Home', 'Products'),
        ('Home', 'Blog'),
        ('Products', 'Contact'),
        ('Blog', 'Home'),
        ('About', 'Contact')
    ]
    
    for source, destination in edges:
        graph.add_edge(source, destination)
    
    print("\nWebsite Link Structure:")
    print(graph)
    print(f"\nPages linked from 'Home': {[n for n, _ in graph.get_neighbors('Home')]}")
    print(f"Pages linking to 'Contact': ", end="")
    pages_to_contact = [v for v in graph.vertices 
                        if any(n == 'Contact' for n, _ in graph.get_neighbors(v))]
    print(pages_to_contact)


def example_3_weighted_graph():
    """Create and explore a weighted graph."""
    print("\n" + "=" * 60)
    print("Example 3: Weighted Graph (Distance Network)")
    print("=" * 60)
    
    # Create a weighted undirected graph
    graph = Graph(
        vertices=['New York', 'Boston', 'Philadelphia', 'Washington DC'],
        is_directed=False,
        is_weighted=True
    )
    
    # Add weighted edges (distances in miles)
    edges = [
        ('New York', 'Boston', 215),
        ('New York', 'Philadelphia', 95),
        ('New York', 'Washington DC', 225),
        ('Philadelphia', 'Washington DC', 140),
        ('Boston', 'Philadelphia', 305)
    ]
    
    for source, destination, weight in edges:
        graph.add_edge(source, destination, weight)
    
    print("\nCity Distance Network:")
    print(graph)
    print(f"\nDistance from New York to Philadelphia: {graph.get_edge_weight('New York', 'Philadelphia')} miles")


def example_4_dynamic_graph_building():
    """Build graph dynamically by adding vertices and edges."""
    print("\n" + "=" * 60)
    print("Example 4: Dynamically Building a Graph")
    print("=" * 60)
    
    # Create empty graph
    graph = Graph(is_directed=True, is_weighted=True)
    
    # Add vertices one by one
    cities = ['Seattle', 'Portland', 'Sacramento', 'Los Angeles']
    for city in cities:
        graph.add_vertex(city)
    
    # Add edges
    routes = [
        ('Seattle', 'Portland', 174),
        ('Portland', 'Sacramento', 635),
        ('Sacramento', 'Los Angeles', 383),
        ('Seattle', 'Sacramento', 840)
    ]
    
    for source, dest, distance in routes:
        graph.add_edge(source, dest, distance)
    
    print("\nFlight Routes (built dynamically):")
    print(graph)


def example_5_graph_properties():
    """Explore various graph properties."""
    print("\n" + "=" * 60)
    print("Example 5: Graph Properties")
    print("=" * 60)
    
    graph = Graph(vertices=['A', 'B', 'C', 'D'], is_directed=False)
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'A')
    
    print(f"\nNumber of vertices: {graph.vertex_count}")
    print(f"Vertices: {graph.vertices}")
    print(f"Is directed: {graph.is_directed}")
    print(f"Is weighted: {graph.is_weighted}")
    print(f"\nAdjacency Matrix:")
    for i, row in enumerate(graph.adj_matrix):
        print(f"  {graph.vertices[i]}: {row}")


if __name__ == "__main__":
    example_1_undirected_graph()
    example_2_directed_graph()
    example_3_weighted_graph()
    example_4_dynamic_graph_building()
    example_5_graph_properties()
    
    print("\n" + "=" * 60)
    print("Graph Basics Overview Complete!")
    print("=" * 60)
