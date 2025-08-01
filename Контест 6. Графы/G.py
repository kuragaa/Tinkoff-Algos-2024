n, m = map(int, input().split())
g = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    g[i][i] = 0
for i in range(m):
    u, v, w = list(map(int, input().split()))
    g[u - 1][v - 1] = w
    g[v - 1][u - 1] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

mn = float('inf')
ans = 0
for i in range(n):
    if max(g[i]) < mn:
        mn = max(g[i])
        ans = i + 1

print(ans)