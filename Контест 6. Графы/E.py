from collections import deque

k = int(input())
g = [[] for _ in range(10 ** 5 + 1)]
for i in range(1, k + 1):
    g[i % k].append([(i + 1) % k, 1])
    g[i % k].append([(10 * i) % k, 0])

q_bfs = deque()
paths = [float('inf') for _ in range(k + 2)]
q_bfs.append([0, 1])
paths[1] = 0

while q_bfs:
    node = q_bfs.popleft()
    for v1, v2 in g[node[1]]:
        if paths[node[1]] + v2 < paths[v1]:
            paths[v1] = paths[node[1]] + v2
            q_bfs.append([paths[v1], v1])

print(paths[0]+1)