"""
5-challenges.py
Practice Challenges with Graph Algorithms

Solve these challenges to master graph algorithms!
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ch19_graph_algorithms.lib.graph import Graph
from ch19_graph_algorithms.lib.traversal import BFS, DFS
from ch19_graph_algorithms.lib.tree import MinimumSpanningTree
from ch19_graph_algorithms.lib.topology import TopologicalSort


# Challenge 1: Social Network Analysis
def challenge_1_social_network():
    """
    Challenge 1: Build a social network and find:
    1. All friends of a person (BFS)
    2. All connections within 2 degrees
    3. Number of friend groups (connected components)
    """
    print("=" * 60)
    print("Challenge 1: Social Network Analysis")
    print("=" * 60)
    
    # Build social network
    graph = Graph(vertices=['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
                 is_directed=False)
    
    friendships = [
        ('Alice', 'Bob'),
        ('Alice', 'Charlie'),
        ('Bob', 'Diana'),
        ('Charlie', 'Diana'),
        ('Eve', 'Frank')
    ]
    
    for person1, person2 in friendships:
        graph.add_edge(person1, person2)
    
    print("\nFriendship Network:")
    print(graph)
    
    # TODO: Implement
    print("\n1. Find all friends of Alice:")
    alice_friends = [n for n, _ in graph.get_neighbors('Alice')]
    print(f"   Answer: {alice_friends}")
    
    print("\n2. Find connected components (friend groups):")
    components = BFS.connected_components(graph)
    print(f"   Number of groups: {len(components)}")
    for i, group in enumerate(components, 1):
        print(f"   Group {i}: {group}")
    
    print("\n3. Find shortest path between two people:")
    start, end = 'Alice', 'Frank'
    path = BFS.shortest_path(graph, start, end)
    if path:
        print(f"   Path from {start} to {end}: {' -> '.join(path)}")
    else:
        print(f"   No connection between {start} and {end}")


# Challenge 2: Web Page Ranking
def challenge_2_web_crawling():
    """
    Challenge 2: Web page crawler
    1. Create a website structure
    2. Find all reachable pages from home
    3. Detect cycles in page links
    """
    print("\n" + "=" * 60)
    print("Challenge 2: Web Site Crawler")
    print("=" * 60)
    
    # Create website
    graph = Graph(vertices=['Home', 'About', 'Products', 'Contact', 'Blog', 'FAQ'],
                 is_directed=True)
    
    links = [
        ('Home', 'About'),
        ('Home', 'Products'),
        ('Home', 'Blog'),
        ('Products', 'Contact'),
        ('Blog', 'Home'),
        ('About', 'Contact'),
        ('FAQ', 'Home')
    ]
    
    for source, dest in links:
        graph.add_edge(source, dest)
    
    print("\nWebsite Structure:")
    print(graph)
    
    print("\n1. Pages reachable from Home:")
    reachable = DFS.traverse(graph, 'Home')
    print(f"   Answer: {reachable}")
    
    print("\n2. Check for link cycles:")
    has_cycle = DFS.has_cycle(graph)
    print(f"   Has cycles: {has_cycle}")


# Challenge 3: Flight Network Optimization
def challenge_3_flight_network():
    """
    Challenge 3: Airline network
    1. Find minimum fuel consumption route (MST)
    2. Find shortest route between cities (BFS on unweighted equivalent)
    """
    print("\n" + "=" * 60)
    print("Challenge 3: Airline Network Optimization")
    print("=" * 60)
    
    graph = Graph(
        vertices=['New York', 'Boston', 'Miami', 'Chicago', 'Denver', 'Los Angeles'],
        is_directed=False,
        is_weighted=True
    )
    
    routes = [
        ('New York', 'Boston', 215),
        ('New York', 'Miami', 1280),
        ('New York', 'Chicago', 790),
        ('Boston', 'Chicago', 980),
        ('Chicago', 'Denver', 1000),
        ('Denver', 'Los Angeles', 1015),
        ('Miami', 'Chicago', 1190),
        ('Los Angeles', 'Denver', 1015)
    ]
    
    for city1, city2, distance in routes:
        graph.add_edge(city1, city2, distance)
    
    print("\nAvailable Flight Routes (distance in miles):")
    for city1, city2, distance in routes:
        print(f"  {city1:15} - {city2:15} : {distance} miles")
    
    print("\n1. Find minimum fuel hub system (MST):")
    mst_edges, total = MinimumSpanningTree.kruskal(graph)
    print(f"   Total minimum distance: {total} miles")
    for c1, c2, dist in mst_edges:
        print(f"   {c1:15} - {c2:15} : {dist} miles")


# Challenge 4: Task Scheduling
def challenge_4_task_scheduling():
    """
    Challenge 4: Project management
    1. Create task dependency graph
    2. Find execution order (topological sort)
    3. Detect circular dependencies
    """
    print("\n" + "=" * 60)
    print("Challenge 4: Project Task Scheduling")
    print("=" * 60)
    
    tasks = ['Design', 'Code', 'Test', 'Deploy', 'Document', 'Review']
    graph = Graph(vertices=tasks, is_directed=True)
    
    dependencies = [
        ('Design', 'Code'),
        ('Code', 'Test'),
        ('Code', 'Review'),
        ('Test', 'Deploy'),
        ('Review', 'Deploy'),
        ('Design', 'Document')
    ]
    
    for task1, task2 in dependencies:
        graph.add_edge(task1, task2)
    
    print("\nTask Dependencies:")
    print(graph)
    
    print("\n1. Recommended execution order:")
    order = TopologicalSort.kahn_algorithm(graph)
    for i, task in enumerate(order, 1):
        print(f"   {i}. {task}")
    
    print("\n2. Check for circular dependencies:")
    try:
        TopologicalSort.kahn_algorithm(graph)
        print("   ✓ No circular dependencies found")
    except ValueError:
        print("   ✗ Circular dependencies detected!")


# Challenge 5: Create Your Own
def challenge_5_custom():
    """
    Challenge 5: Create your own graph problem
    
    Ideas:
    - Transportation network
    - Game level dependencies
    - Social media recommendation
    - Electrical grid connections
    - Family tree relationships
    """
    print("\n" + "=" * 60)
    print("Challenge 5: Create Your Own Graph Problem")
    print("=" * 60)
    
    print("\nPossible Ideas:")
    print("1. Transportation/Delivery network")
    print("2. Game or application feature dependencies")
    print("3. Social network recommendation system")
    print("4. Electrical grid or network connections")
    print("5. Family tree or organizational hierarchy")
    
    print("\nTODO: Create your own graph and solve a problem using:")
    print("- Graph creation and manipulation")
    print("- Traversal algorithms (BFS/DFS)")
    print("- Spanning trees")
    print("- Topological sorting")


if __name__ == "__main__":
    challenge_1_social_network()
    challenge_2_web_crawling()
    challenge_3_flight_network()
    challenge_4_task_scheduling()
    challenge_5_custom()
    
    print("\n" + "=" * 60)
    print("Challenge Problems Complete!")
    print("=" * 60)
