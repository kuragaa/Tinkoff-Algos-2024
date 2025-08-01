import math

def precompute_lca(n, edges):
    logn = int(math.ceil(math.log2(n)))
    
    up = [[0] * logn for _ in range(n)]
    
    tin = [0] * n
    tout = [0] * n
    t = 0 
    
    def dfs(v):
        nonlocal t
        tin[v] = t
        t += 1
        for u in edges[v]:
            up[u][0] = v
            dfs(u)
        tout[v] = t
    
    dfs(0)
    
    for l in range(1, logn):
        for v in range(n):
            up[v][l] = up[up[v][l - 1]][l - 1]
    
    return up, tin, tout

def is_ancestor(u, v, tin, tout):
    return tin[u] <= tin[v] and tout[u] >= tout[v]

def find_lca(u, v, up, tin, tout):
  
    if is_ancestor(u, v, tin, tout):
        return u
    
    if is_ancestor(v, u, tin, tout):
        return v
    
    logn = len(up[0])
    for l in range(logn - 1, -1, -1):
        if not is_ancestor(up[u][l], v, tin, tout):
            u = up[u][l]
    return up[u][0]


n = int(input())
parents = list(map(int, input().split()))
m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

edges = [[] for _ in range(n)]
for i, p in enumerate(parents):
    edges[p].append(i + 1)

up, tin, tout = precompute_lca(n, edges)

for u, v in queries:
    lca = find_lca(u, v, up, tin, tout)
    print(lca)