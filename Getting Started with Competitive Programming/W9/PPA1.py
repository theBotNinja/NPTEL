from collections import defaultdict

# Helper function to perform DFS for augmenting paths
def bpm(u, matchU, matchV, visited, adj):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            if matchV[v] == -1 or bpm(matchV[v], matchU, matchV, visited, adj):
                matchU[u] = v
                matchV[v] = u
                return True
    return False

# Function to find maximum bipartite matching using DFS
def max_bipartite_matching(n, adj):
    matchU = [-1] * n
    matchV = [-1] * n
    result = 0
    for u in range(n):
        visited = [False] * n
        if bpm(u, matchU, matchV, visited, adj):
            result += 1
    return result

# Read input
n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Step 1: Convert the graph into a bipartite graph representation
adj = defaultdict(list)

for u, v in edges:
    adj[u - 1].append(v - 1)  # Create edges in the bipartite graph

# Step 2: Find maximum bipartite matching
max_matching = max_bipartite_matching(n, adj)

# Step 3: Calculate the minimum path cover
min_path_cover = n - max_matching

# Step 4: Output result
if min_path_cover <= k:
    print("YES")
else:
    print("NO")
