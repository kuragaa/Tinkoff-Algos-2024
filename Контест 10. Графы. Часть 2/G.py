import sys
sys.setrecursionlimit(10000)
from heapq import heappush, heappop

def dijkstra(g, start, a, b, c):
    dist = [float('inf')] * n
    dist[start] = 0
    q = [(0, start)]
    while q:
        d, u = heappop(q)
        for v, l in g[u]:
            if dist[v] > d + l:
                dist[v] = d + l
                heappush(q, (dist[v], v))
    global res
    res = min(res, dist[a] + dist[b] + dist[c])
    return res

def find(g, a, b, c):
    if dijkstra(g, a-1, a-1, b-1, c-1) == float('inf'):
        print(-1)
    else:
        dijkstra(g, b-1, a-1, b-1, c-1)
        dijkstra(g, c-1, a-1, b-1, c-1)
        print(res)

global res
res = float('inf')
n, m = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n)]
for i in range(m):
    b, e, w = map(int, sys.stdin.readline().split())
    g[b-1].append((e-1, w))
    g[e-1].append((b-1, w))
a, b, c = map(int, sys.stdin.readline().split())
find(g, a, b, c)