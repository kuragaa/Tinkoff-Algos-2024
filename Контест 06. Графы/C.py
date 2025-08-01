from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
in_degree = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

for u in g:
    for v in g[u]:
        in_degree[v] += 1

# print(g)
# print(in_degree)

check = list(map(int, input().split()))

for i in range(n):
    if in_degree[check[i]] != 0:
        print('NO')
        break
    for v in g[check[i]]:
        in_degree[v] -= 1
else:
    print('YES')