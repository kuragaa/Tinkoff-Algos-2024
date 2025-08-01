import sys

def build(g, d, dp, mxd, v, u=0, c=float('inf')):
    if u != v:
        d[v] = d[u] + 1
    dp[v][0] = (u, c)
    for i in range(1, mxd + 1):
        dp[v][i] = (dp[dp[v][i - 1][0]][i - 1][0], min(dp[v][i - 1][1], dp[dp[v][i - 1][0]][i - 1][1]))
    for nxt, cost in g[v]:
        build(g, d, dp, mxd, nxt, v, cost)

def find_lca(d, dp, mxd, u, v):
    lca = float('inf')
    if d[u] < d[v]:
        u, v = v, u
    for i in range(mxd, -1, -1):
        if d[v] <= d[dp[u][i][0]]:
            lca = min(lca, dp[u][i][1])
            u = dp[u][i][0]
    if v == u:
        return lca
    for i in range(mxd, -1, -1):
        if dp[u][i][0] != dp[v][i][0]:
            lca = min(lca, dp[v][i][1])
            v = dp[v][i][0]
            lca = min(lca, dp[u][i][1])
            u = dp[u][i][0]
    lca = min(lca, dp[v][0][1])
    lca = min(lca, dp[u][0][1])

    return lca


n = int(sys.stdin.readline())
g = [[] for _ in range(n)]
for i in range(1, n):
    x, y = map(int, sys.stdin.readline().split())
    g[x].append((i, y))

d = [0] * n
dp = [[] for _ in range(n)]
mxd = 0
while (1 << mxd) <= n:
    mxd += 1
for i in range(n):
    dp[i] = [(-1, float('inf'))] * (mxd + 1)

build(g, d, dp, mxd, 0)

m = int(sys.stdin.readline())
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    print(find_lca(d, dp, mxd, u, v))