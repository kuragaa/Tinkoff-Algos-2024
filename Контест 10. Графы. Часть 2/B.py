import sys
from heapq import heappush, heappop

def prim_ans(g):
    used = [False] * len(g)
    min_edge = [float('inf')] * len(g)
    min_v = [-1] * len(g)
    min_edge[0] = 0
    q = [(0, 0)]
    res = 0

    while q:
        w, u = heappop(q)
        if not used[u]:
            res += w
            used[u] = True
            for v, edge_w in g[u]:
                if not used[v] and edge_w < min_edge[v]:
                    min_edge[v] = edge_w
                    min_v[v] = u
                    heappush(q, (edge_w, v))

    return res

n, m = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n)]
for i in range(m):
    b, e, w = map(int, sys.stdin.readline().split())
    g[b-1].append((e-1, w))
    g[e-1].append((b-1, w))

print(prim_ans(g))