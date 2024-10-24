from collections import deque

# BFS to find the path with available capacity
def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in range(len(capacity)):
            if v not in visited and capacity[u][v] > 0:  # Check for available capacity
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
                visited.add(v)
    
    return False

# Edmonds-Karp Algorithm to find the maximum flow
def edmonds_karp(capacity, source, sink):
    parent = [-1] * len(capacity)  # To store the path
    max_flow = 0
    
    # Augment flow while there is a path from source to sink
    while bfs(capacity, source, sink, parent):
        # Find the maximum flow through the path found by BFS
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        # Update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

# Read input
E = int(input())  # Number of edges
edges = []
nodes = set()

for _ in range(E):
    u, v, w = input().split()
    w = int(w)
    edges.append((u, v, w))
    nodes.add(u)
    nodes.add(v)

# Create a mapping from nodes to indices
node_list = list(nodes)
node_map = {node: idx for idx, node in enumerate(node_list)}

# Create a capacity matrix
n = len(nodes)
capacity = [[0] * n for _ in range(n)]

# Fill the capacity matrix with input edges
for u, v, w in edges:
    capacity[node_map[u]][node_map[v]] += w

# Find the max flow
source = node_map['S']
sink = node_map['T']
max_flow = edmonds_karp(capacity, source, sink)

# Output the result
print(max_flow)
