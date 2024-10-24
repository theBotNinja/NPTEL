import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent, depth, adj, v, d, flip_even, flip_odd):
    global flip_count
    # If we are at an even depth and flip_even is set or at odd depth and flip_odd is set,
    # we need to flip the value.
    current_value = v[node] ^ (flip_even if depth % 2 == 0 else flip_odd)
    
    # If the current value does not match the desired value, we need to flip this node.
    if current_value != d[node]:
        flip_count += 1
        if depth % 2 == 0:
            flip_even ^= 1
        else:
            flip_odd ^= 1
        result.append(node)
    
    # Traverse all the children (adjacent nodes) of the current node
    for child in adj[node]:
        if child != parent:
            dfs(child, node, depth + 1, adj, v, d, flip_even, flip_odd)

def solve():
    n = int(input())
    adj = [[] for _ in range(n)]
    
    # Read the tree edges
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    # Read initial and desired values
    v = list(map(int, input().split()))
    d = list(map(int, input().split()))
    
    # We start DFS from the root (node 0)
    dfs(0, -1, 0, adj, v, d, 0, 0)
    
    # Print the result
    print(flip_count)

# Global variables to track the flips
flip_count = 0
result = []

# Solve the problem
solve()
