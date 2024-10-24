import heapq

INF = 10**18

def dijkstra(n, graph, start):
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def solve():
    n, m, L, s, t = map(int, input().split())
    edges = []
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        if w > 0:
            graph[u].append((v, w))
            graph[v].append((u, w))
    
    # Run Dijkstra without the missing edges (with weight 0)
    dist_from_s = dijkstra(n, graph, s)
    dist_from_t = dijkstra(n, graph, t)
    
    # Check if it's impossible with current edges
    if dist_from_s[t] < L:
        print("NO")
        return
    if dist_from_s[t] == L:
        print("YES")
        for u, v, w in edges:
            if w == 0:
                print(u, v, L + 1)
            else:
                print(u, v, w)
        return
    
    # Add missing edges with very small weight (1) and very large weight
    low = 1
    high = INF
    new_graph = [[] for _ in range(n)]
    
    for u, v, w in edges:
        if w == 0:
            new_graph[u].append((v, low))
            new_graph[v].append((u, low))
        else:
            new_graph[u].append((v, w))
            new_graph[v].append((u, w))
    
    dist_from_s_low = dijkstra(n, new_graph, s)
    
    if dist_from_s_low[t] > L:
        print("NO")
        return
    
    # Binary search to find the right weight for edges with w = 0
    low = 1
    high = L
    while low < high:
        mid = (low + high + 1) // 2
        new_graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            if w == 0:
                new_graph[u].append((v, mid))
                new_graph[v].append((u, mid))
            else:
                new_graph[u].append((v, w))
                new_graph[v].append((u, w))
        
        dist_from_s_mid = dijkstra(n, new_graph, s)
        
        if dist_from_s_mid[t] <= L:
            low = mid
        else:
            high = mid - 1
    
    print("YES")

# Main Execution
solve()
