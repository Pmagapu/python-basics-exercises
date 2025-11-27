"""
4-topological-sort-examples.py
Understanding Topological Sort

This file demonstrates:
- DFS-based Topological Sort
- Kahn's Algorithm (BFS-based)
- Cycle detection
- Finding longest path in DAG
- Real-world applications
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ch19_graph_algorithms.lib.graph import Graph
from ch19_graph_algorithms.lib.topology import TopologicalSort


def example_1_basic_topological_sort():
    """Demonstrate basic topological sort."""
    print("=" * 60)
    print("Example 1: Basic Topological Sort")
    print("=" * 60)
    
    # Create a directed acyclic graph (DAG)
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E'], 
                 is_directed=True, is_weighted=False)
    
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('D', 'E')
    ]
    
    for source, dest in edges:
        graph.add_edge(source, dest)
    
    print("\nDirected Acyclic Graph (DAG):")
    print(graph)
    
    # DFS-based topological sort
    dfs_topo = TopologicalSort.dfs_based(graph)
    print(f"\nTopological Order (DFS-based): {' -> '.join(dfs_topo)}")
    
    # Kahn's algorithm
    kahn_topo = TopologicalSort.kahn_algorithm(graph)
    print(f"Topological Order (Kahn's):    {' -> '.join(kahn_topo)}")


def example_2_course_prerequisites():
    """Real-world example: Course prerequisites."""
    print("\n" + "=" * 60)
    print("Example 2: Course Prerequisites (Real-world Application)")
    print("=" * 60)
    
    # Build a course dependency graph
    courses = [
        'Python Basics',
        'Data Structures',
        'Algorithms',
        'Web Development',
        'Database Design',
        'Full Stack Development'
    ]
    
    graph = Graph(vertices=courses, is_directed=True)
    
    # Prerequisites (directed edges show: if B depends on A, add A->B)
    prerequisites = [
        ('Python Basics', 'Data Structures'),
        ('Python Basics', 'Web Development'),
        ('Data Structures', 'Algorithms'),
        ('Data Structures', 'Database Design'),
        ('Algorithms', 'Full Stack Development'),
        ('Web Development', 'Full Stack Development'),
        ('Database Design', 'Full Stack Development')
    ]
    
    for prereq, course in prerequisites:
        graph.add_edge(prereq, course)
    
    print("\nCourse Dependency Graph:")
    for course in courses:
        deps = [dest for dest, _ in graph.get_neighbors(course)]
        if deps:
            print(f"  {course} must be taken before: {', '.join(deps)}")
    
    print("\nRecommended Course Order:")
    order = TopologicalSort.kahn_algorithm(graph)
    for i, course in enumerate(order, 1):
        print(f"  {i}. {course}")


def example_3_build_system():
    """Real-world example: Build system with dependencies."""
    print("\n" + "=" * 60)
    print("Example 3: Build System (Real-world Application)")
    print("=" * 60)
    
    # Build tasks with dependencies
    tasks = ['SourceFiles', 'CompileC', 'CompileJava', 'LinkObjects', 
             'GenerateDocs', 'PackageApp', 'DeployApp']
    
    graph = Graph(vertices=tasks, is_directed=True)
    
    # Task dependencies (A must complete before B)
    dependencies = [
        ('SourceFiles', 'CompileC'),
        ('SourceFiles', 'CompileJava'),
        ('CompileC', 'LinkObjects'),
        ('CompileJava', 'LinkObjects'),
        ('SourceFiles', 'GenerateDocs'),
        ('LinkObjects', 'PackageApp'),
        ('GenerateDocs', 'PackageApp'),
        ('PackageApp', 'DeployApp')
    ]
    
    for task1, task2 in dependencies:
        graph.add_edge(task1, task2)
    
    print("\nBuild Task Dependencies:")
    print(graph)
    
    print("\nBuild Execution Order:")
    order = TopologicalSort.kahn_algorithm(graph)
    for i, task in enumerate(order, 1):
        print(f"  {i}. {task}")


def example_4_cycle_detection():
    """Detect cycles in directed graphs."""
    print("\n" + "=" * 60)
    print("Example 4: Cycle Detection in Task Dependencies")
    print("=" * 60)
    
    # Valid DAG
    print("\nGraph 1 (Valid - No cycles):")
    graph1 = Graph(vertices=['Task1', 'Task2', 'Task3', 'Task4'],
                  is_directed=True)
    edges1 = [('Task1', 'Task2'), ('Task2', 'Task3'), ('Task1', 'Task4')]
    
    for source, dest in edges1:
        graph1.add_edge(source, dest)
    
    print(graph1)
    try:
        order1 = TopologicalSort.kahn_algorithm(graph1)
        print(f"✓ Valid topological order: {' -> '.join(order1)}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    # Graph with cycle
    print("\nGraph 2 (Invalid - Has cycle):")
    graph2 = Graph(vertices=['Task1', 'Task2', 'Task3', 'Task4'],
                  is_directed=True)
    edges2 = [
        ('Task1', 'Task2'),
        ('Task2', 'Task3'),
        ('Task3', 'Task4'),
        ('Task4', 'Task2')  # Creates cycle: Task2 -> Task3 -> Task4 -> Task2
    ]
    
    for source, dest in edges2:
        graph2.add_edge(source, dest)
    
    print(graph2)
    try:
        order2 = TopologicalSort.kahn_algorithm(graph2)
        print(f"✓ Valid topological order: {' -> '.join(order2)}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def example_5_longest_path():
    """Find longest path in a DAG (project scheduling)."""
    print("\n" + "=" * 60)
    print("Example 5: Critical Path (Longest Path in DAG)")
    print("=" * 60)
    
    # Project tasks with durations
    activities = [
        'Start', 'Design', 'Development', 'Testing',
        'Documentation', 'Review', 'Deploy', 'End'
    ]
    
    graph = Graph(vertices=activities, is_directed=True, is_weighted=True)
    
    # Task sequences with durations (in days)
    sequence = [
        ('Start', 'Design', 5),
        ('Design', 'Development', 15),
        ('Design', 'Documentation', 3),
        ('Development', 'Testing', 10),
        ('Documentation', 'Review', 2),
        ('Testing', 'Review', 5),
        ('Review', 'Deploy', 1),
        ('Deploy', 'End', 0)
    ]
    
    for source, dest, duration in sequence:
        graph.add_edge(source, dest, duration)
    
    print("\nProject Activities with Durations:")
    for source, dest, duration in sequence:
        print(f"  {source:15} -> {dest:15} : {duration} days")
    
    print("\nFinding Critical Path (longest path)...")
    max_duration, path = TopologicalSort.find_longest_path(graph)
    
    print(f"\nCritical Path (longest duration): {max_duration} days")
    print(f"Path: {' -> '.join(path)}")
    print("\nThis is the minimum project completion time!")


def example_6_algorithm_comparison():
    """Compare DFS-based and Kahn's algorithm."""
    print("\n" + "=" * 60)
    print("Example 6: Algorithm Comparison (DFS vs Kahn)")
    print("=" * 60)
    
    graph = Graph(vertices=['A', 'B', 'C', 'D', 'E', 'F'],
                 is_directed=True)
    
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'E'),
        ('D', 'F'),
        ('E', 'F')
    ]
    
    for source, dest in edges:
        graph.add_edge(source, dest)
    
    print("\nDirected Acyclic Graph:")
    print(graph)
    
    dfs_result = TopologicalSort.dfs_based(graph)
    kahn_result = TopologicalSort.kahn_algorithm(graph)
    
    print(f"\nDFS-based:  {' -> '.join(dfs_result)}")
    print(f"Kahn's:     {' -> '.join(kahn_result)}")
    print("\nBoth produce valid topological orders (may differ)")
    print("Kahn's is often preferred for detecting cycles explicitly")


if __name__ == "__main__":
    example_1_basic_topological_sort()
    example_2_course_prerequisites()
    example_3_build_system()
    example_4_cycle_detection()
    example_5_longest_path()
    example_6_algorithm_comparison()
    
    print("\n" + "=" * 60)
    print("Topological Sort Examples Complete!")
    print("=" * 60)
