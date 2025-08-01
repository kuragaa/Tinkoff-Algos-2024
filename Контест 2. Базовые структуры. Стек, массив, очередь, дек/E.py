n = int(input())
wagons = list(map(int, input().split()))
deadend = []
op = []
num = 1

for w in wagons:
    if len(deadend) != 0 and w > deadend[-1]:
        print(0)
        quit()
    deadend.append(w)
    op.append(1)
    while len(deadend) != 0 and deadend[-1] == num:
        deadend.pop()
        op.append(2)
        num += 1
cur = 1
cnt = 0
res = []
for el in op:
    if el == cur:
        cnt += 1
    else:
        res.append([cur, cnt])
        cur = el
        cnt = 1
res.append([cur, cnt])

print(len(res))
for el in res:
    print(*el)