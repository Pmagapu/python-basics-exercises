# Chapter 19: Graph Algorithms

A comprehensive Python library for learning and implementing popular graph algorithms. This chapter provides educational examples and reusable algorithm implementations.

## Overview

This library includes implementations of essential graph algorithms used in computer science and real-world applications.

### Algorithms Included

1. **Breadth-First Search (BFS)**
   - Level-order traversal
   - Shortest path in unweighted graphs
   - Finding connected components
   - Time: O(V + E), Space: O(V)

2. **Depth-First Search (DFS)**
   - Deep traversal with backtracking
   - Cycle detection in directed graphs
   - Used in topological sorting
   - Time: O(V + E), Space: O(V)

3. **Minimum Spanning Tree (MST)**
   - **Kruskal's Algorithm**: Greedy, edge-based, uses Union-Find
   - **Prim's Algorithm**: Incremental vertex-based approach
   - Time: O(E log E) for Kruskal's, O(V²) for Prim's
   - Applications: Network design, utility connections

4. **Topological Sort**
   - **DFS-based**: Uses recursion and finishing times
   - **Kahn's Algorithm**: BFS-based using in-degrees
   - For Directed Acyclic Graphs (DAGs) only
   - Applications: Task scheduling, course prerequisites
   - Time: O(V + E), Space: O(V)

## Directory Structure

```
ch19-graph-algorithms/
├── lib/                          # Reusable library modules
│   ├── __init__.py
│   ├── graph.py                  # Core graph data structure
│   ├── traversal.py              # BFS and DFS algorithms
│   ├── tree.py                   # MST algorithms (Kruskal, Prim)
│   └── topology.py               # Topological sort algorithms
├── 1-graph-basics.py             # Learn graph fundamentals
├── 2-traversal-examples.py       # BFS and DFS examples
├── 3-spanning-tree-examples.py   # MST examples
├── 4-topological-sort-examples.py# Topological sort examples
├── 5-challenges.py               # Practice problems
└── README.md                     # This file
```

## Core Classes

### Graph

Main data structure with support for:
- Directed and undirected graphs
- Weighted and unweighted edges
- Both adjacency list and adjacency matrix representations

```python
from ch19_graph_algorithms.lib.graph import Graph

# Create undirected, unweighted graph
graph = Graph(vertices=['A', 'B', 'C'], is_directed=False, is_weighted=False)
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
```

### Traversal Algorithms

BFS and DFS implementations:

```python
from ch19_graph_algorithms.lib.traversal import BFS, DFS

# BFS traversal
order = BFS.traverse(graph, 'A')  # ['A', 'B', 'C', ...]

# Shortest path (unweighted)
path = BFS.shortest_path(graph, 'A', 'C')

# Connected components
components = BFS.connected_components(graph)

# Cycle detection
has_cycle = DFS.has_cycle(graph)
```

### Minimum Spanning Tree

Kruskal's and Prim's algorithms:

```python
from ch19_graph_algorithms.lib.tree import MinimumSpanningTree

# Kruskal's algorithm
mst_edges, total_weight = MinimumSpanningTree.kruskal(graph)

# Prim's algorithm
mst_edges, total_weight = MinimumSpanningTree.prim(graph, start_vertex='A')
```

### Topological Sort

For directed acyclic graphs:

```python
from ch19_graph_algorithms.lib.topology import TopologicalSort

# DFS-based topological sort
order = TopologicalSort.dfs_based(dag)

# Kahn's algorithm
order = TopologicalSort.kahn_algorithm(dag)

# Find longest path (critical path)
distance, path = TopologicalSort.find_longest_path(dag)
```

## Example Files

### 1-graph-basics.py
Introduction to graphs:
- Creating undirected and directed graphs
- Weighted vs unweighted graphs
- Graph representations (adjacency list, matrix)
- Dynamic graph building

### 2-traversal-examples.py
Traversal techniques:
- BFS traversal and level-order visits
- DFS traversal (recursive and iterative)
- Finding shortest paths
- Connected components
- Cycle detection

### 3-spanning-tree-examples.py
Minimum spanning trees:
- Kruskal's algorithm with Union-Find
- Prim's algorithm with greedy selection
- Network design application
- Road network optimization
- Algorithm comparison

### 4-topological-sort-examples.py
Topological sorting:
- Basic topological ordering
- Course prerequisites
- Build system dependencies
- Cycle detection in dependencies
- Critical path analysis (longest path)
- Kahn's algorithm for cycle detection

### 5-challenges.py
Practice problems:
- Social network analysis
- Web crawler and link detection
- Flight network optimization
- Task scheduling with dependencies
- Create your own problems

## Running the Examples

Each example file can be run independently:

```bash
# Run graph basics
python ch19-graph-algorithms/1-graph-basics.py

# Run traversal examples
python ch19-graph-algorithms/2-traversal-examples.py

# Run spanning tree examples
python ch19-graph-algorithms/3-spanning-tree-examples.py

# Run topological sort examples
python ch19-graph-algorithms/4-topological-sort-examples.py

# Run challenge problems
python ch19-graph-algorithms/5-challenges.py
```

## Real-World Applications

### BFS/DFS
- Social networks (friend connections)
- Web crawlers (page discovery)
- Game maps (pathfinding)
- Dependency trees

### Minimum Spanning Trees
- Network design (minimize cable)
- Electrical grid connections
- Road networks
- Telecommunications infrastructure

### Topological Sort
- Project scheduling
- Build systems
- Course prerequisites
- Instruction sequencing
- Dependency resolution

## Key Concepts

### Time and Space Complexity

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| BFS | O(V+E) | O(V) | Shortest unweighted path |
| DFS | O(V+E) | O(V) | Cycle detection |
| Kruskal's | O(E log E) | O(V) | MST (edge-based) |
| Prim's | O(V²) | O(V) | MST (vertex-based) |
| Topological Sort | O(V+E) | O(V) | DAG ordering |

### Graph Terminology

- **Vertex**: Node in the graph
- **Edge**: Connection between vertices
- **Directed**: Edges have direction (one-way)
- **Undirected**: Edges have no direction (two-way)
- **Weighted**: Edges have associated values
- **Cycle**: Path that starts and ends at same vertex
- **DAG**: Directed Acyclic Graph (no cycles)
- **Connected**: All vertices reachable from any vertex
- **Spanning Tree**: Tree connecting all vertices with V-1 edges

## Learning Path

1. Start with **1-graph-basics.py** to understand graph structures
2. Continue with **2-traversal-examples.py** for BFS and DFS
3. Learn **3-spanning-tree-examples.py** for MST algorithms
4. Study **4-topological-sort-examples.py** for DAG ordering
5. Practice with **5-challenges.py**

## Tips for Learning

- Understand the graph representation first
- Trace through algorithms step-by-step
- Visualize graphs on paper while learning
- Start with small examples
- Relate to real-world applications
- Compare different algorithms on same graph
- Implement variations yourself

## Common Pitfalls

- Forgetting to mark vertices as visited (infinite loops)
- Not handling directed vs undirected correctly
- Assuming all graphs are connected
- Topological sort only for DAGs (no cycles)
- Confusing edge direction in directed graphs
- Not considering self-loops
- Assuming MST is unique (multiple valid MSTs possible)

## Further Exploration

- Dijkstra's algorithm (shortest path with weights)
- Bellman-Ford algorithm (negative weights)
- Floyd-Warshall algorithm (all pairs shortest paths)
- Strongly connected components
- Bipartite graph checking
- Coloring problems
- Maximum flow algorithms

## References

- Graph Theory fundamentals
- Algorithm design patterns
- Data structure optimization
- Real-world graph applications
