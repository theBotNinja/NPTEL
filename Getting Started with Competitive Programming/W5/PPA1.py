def min_groups(n, parents):
    depth = [-1] * n

    def compute_depth(v):
        if depth[v] != -1:
            return depth[v]
        if parents[v] == -1:
            depth[v] = 1
        else:
            depth[v] = compute_depth(parents[v] - 1) + 1
        return depth[v]

    max_depth = 0
    for i in range(n):
        max_depth = max(max_depth, compute_depth(i))

    return max_depth

n = int(input())
parents = [int(input()) for i in range(n)]
print(min_groups(n, parents))
