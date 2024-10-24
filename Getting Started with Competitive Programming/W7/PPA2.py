class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    uf = UnionFind(n)
    mst_weight = 0
    edge_count = 0
    
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
            edge_count += 1
            if edge_count == n - 1:
                break
    
    return mst_weight

# Read input
n, m = map(int, input().split())
edges = []
total_weight = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))  # Use zero-indexed nodes
    total_weight += w  # Add the weight to the total weight

# Calculate the MST weight using Kruskal's algorithm
mst_weight = kruskal(n, edges)

# The maximum length of roads that can be broken
max_broken_length = total_weight - mst_weight

# Output the result
print(max_broken_length)
