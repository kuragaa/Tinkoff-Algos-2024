import sys
sys.setrecursionlimit(10000)

def get(x):
    if nodes[x] < 0:
        return x
    else:
        root = get(nodes[x])
        nodes[x] = root
        return root

def union(x, y):
    x = get(x)
    y = get(y)
    if x == y:
        return False
    if nodes[x] > nodes[y]:
        nodes[y] += nodes[x]
        nodes[x] = y
    else:
        nodes[x] += nodes[y]
        nodes[y] = x
    return True

def shift(i, j):
    return j + i * (V + 1)

K, V = map(int, input().split())
nodes = [-1] * (shift(K + 1, V) + 1)
for i in range(1, K + 1):
    for j, num in enumerate(map(int, input().split()), start=1):
        if num & 1:
            union(shift(i, j), shift(i + 1, j))
        if num & 2:
            union(shift(i, j), shift(i, j + 1))

Ks, Vs, Ds, cost = [], [], [], 0
for i in range(1, K):
    for j in range(1, V + 1):
        if union(shift(i, j), shift(i + 1, j)):
            cost += 1
            Ks.append(i)
            Vs.append(j)
            Ds.append(1)

for i in range(1, K + 1):
    for j in range(1, V):
        if union(shift(i, j), shift(i, j + 1)):
            cost += 2
            Ks.append(i)
            Vs.append(j)
            Ds.append(2)

print(len(Ks), cost)
for i in range(len(Ks)):
    print(Ks[i], Vs[i], Ds[i])