def update(i):
    while i <= n:
        tree[i] += 1
        i = i + (i & -i)

def summ(i):
    ttl = 0
    while i > 0:
        ttl += tree[i]
        i = i - (i & -i)
    return ttl

n = int(input())
army = list(map(int, input().split()))
i_army = [(a, i) for i, a in enumerate(army, 1)]
i_army.sort(reverse=True)
idx = [0] * (n + 1)
tree = [0] * (n + 1)
res = 0

for i in range(1, n + 1):
    idx[i_army[i - 1][1]] = i

for i in range(1, n + 1):
    sub = summ(idx[i])
    res += sub * (n - i - idx[i] + sub + 1)
    update(idx[i])

print(res)