import sys
sys.setrecursionlimit(10**5)

def dfs(v, c):
    visited[v] = c
    comp_vs.append(v)
    for k in g[v]:
        if visited[k] == 0:
            dfs(k, c)


n, m = map(int, input().split())
g = [[] for i in range(n+1)]
for i in range(1, m+1):
    f, t = map(int, input().split())
    g[f].append(t)
    g[t].append(f)

visited = [0 for _ in range(n+1)]

comp_num = 1
ans = []
for i in range(1, n+1):
    if visited[i] == 0:
        comp_vs = []
        dfs(i, comp_num)
        ans.append(sorted(comp_vs))
        comp_num += 1

print(len(ans))
for i in ans:
    print(len(i))
    print(*i)