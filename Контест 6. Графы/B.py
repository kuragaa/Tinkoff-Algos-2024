def dfs(node, status):
    status[node] = 1
    for neighbor in g[node]:
        if status[neighbor] == 0:
            if dfs(neighbor, status):
                return True
        elif status[neighbor] == 1:
            return True
    status[node] = 2
    return False

n, m = map(int, input().split())
g = [set() for _ in range(n)]
for _ in range(m):
    f, t = map(int, input().split())
    g[f - 1].add(t - 1)

status = [0]*len(g)
for i in range(len(g)):
    if status[i] == 0:
        if dfs(i, status):
            print(1)
            break
else:
    print(0)