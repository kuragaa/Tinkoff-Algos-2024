import sys

sys.setrecursionlimit(10**5+7000)

def dfs_with_counting_max_distance(node, count):
  global visited, x, maxCount, nodes_connections, depths
  visited[node] = 1
  count += 1
  for i in nodes_connections[node]:
    if visited[i] == 0:
      depths[i] = count
      if count >= maxCount:
        maxCount = count
        x = i
      dfs_with_counting_max_distance(i, count)


def dfs(node, n):
  count = 0
  for i in range(n + 1):
    visited[i] = 0

  dfs_with_counting_max_distance(node, count)


def diameter(n):
  global nodes_connections, maxCount, ans_depths
  dfs(0, n)
  ans_depths = depths.copy()
  dfs(x, n)
  return maxCount


n = int(input())
nodes = [int(i) for i in input().split()]
nodes_connections, visited = [[] for _ in range(n + 1)], [0 for _ in range(n + 1)]
depths, ans_depths = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(n - 1):
  nodes_connections[nodes[i]].append(i + 1)
  nodes_connections[i + 1].append(nodes[i])

maxCount = -10 ** 19
x = 0
diameter = diameter(n)
print(max(ans_depths), diameter)
print(*ans_depths[:n])