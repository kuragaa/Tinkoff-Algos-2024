def get(x):
    if x == nodes[x]:
        return x
    nodes[x] = get(nodes[x])
    return nodes[x]

def union(x, y):
    x = get(x)
    y = get(y)
    if x == y:
        return
    if d[y] > d[x]:
        x, y = y, x
    nodes[y] = x
    if d[x] == d[y]:
        d[x] += 1
    maxx[x] = max(maxx[x], maxx[y])
    minn[x] = min(minn[x], minn[y])
    cnt[x] += cnt[y]

n, m = map(int, input().split())
nodes, minn, maxx, cnt, d = [0], [0], [0], [1]*(n+1), [0]*(n+1)
for i in range(1, n+1):
    nodes.append(i)
    minn.append(i)
    maxx.append(i)
for _ in range(m):
    op = input().split()
    if op[0] == 'union':
        union(int(op[1]), int(op[2]))
    else:
        target = get(int(op[1]))
        print(minn[target], maxx[target], cnt[target])