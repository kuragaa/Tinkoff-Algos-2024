import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n)]
for i in range(m):
    b, e, w = map(int, sys.stdin.readline().split())
    g[b-1].append((e-1, w))
    g[e-1].append((b-1, w))

dist = [float('inf')] * n
dist[0] = 0
q = [(0, 0)]
while q:
    d, u = heapq.heappop(q)
    for v, l in g[u]:
        if dist[v] > d + l:
            dist[v] = d + l
            heapq.heappush(q, (d + l, v))

print(*dist)