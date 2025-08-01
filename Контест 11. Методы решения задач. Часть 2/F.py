from itertools import *

n, m = map(int, input().split())
summa = 0
cost = [int(i) for i in input().split()]
ans = 0
minn = 1000000
for k in product('012', repeat=m):
    summa = 0
    cnt = 0
    i = 0
    for j in k:
        cnt += int(j)
        summa += cost[i] * int(j)
        i += 1
    if summa == n:
        if minn > cnt:
            minn = cnt
            ans = k
    if ''.join(k) == '2' * m and summa < n:
        print(-1)
        exit(0)
if ans == 0:
    print(0)
else:
    print(minn)
    for i in range(m):
        for j in range(int(ans[i])):
            print(cost[int(i)], end=' ')