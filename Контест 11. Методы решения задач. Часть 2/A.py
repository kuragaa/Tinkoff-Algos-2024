import sys

def build(g, d, dp, mxd, v, u=0):
    if u != v:
        d[v] = d[u] + 1
    dp[v][0] = u
    for i in range(1, mxd + 1):
        dp[v][i] = dp[dp[v][i - 1]][i - 1]
    for nxt in g[v]:
        build(g, d, dp, mxd, nxt, v)

def find_lca(d, dp, mxd, u, v):
    if d[u] < d[v]:
        u, v = v, u
    for i in range(mxd, -1, -1):
        if d[v] <= d[dp[u][i]]:
            u = dp[u][i]
    if v == u:
        return v
    for i in range(mxd, -1, -1):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]

    return dp[v][0]


n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
g = [[] for _ in range(n)]
for i in range(1, n):
    g[parents[i - 1]].append(i)

d = [0] * n
dp = [[] for _ in range(n)]
mxd = 0
while (1 << mxd) <= n:
    mxd += 1
for i in range(n):
    dp[i] = [-1] * (mxd + 1)

build(g, d, dp, mxd, 0)

m = int(sys.stdin.readline())
for _ in range(m):
    u, v = map(int, input().split())
    print(find_lca(d, dp, mxd, u, v))