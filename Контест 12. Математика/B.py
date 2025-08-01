import math
import sys
sys.setrecursionlimit(10000)

def primes(n):
    res = []
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    if cnt > 0:
        res.append((2, cnt))

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt > 0:
            res.append((i, cnt))

    if n > 1:
        res.append((n, 1))

    return res

n = int(input().strip())
primes_arr = primes(n)
ans = []
for base, exp in primes_arr:
    if exp == 1:
        ans.append(f"{base}")
    else:
        ans.append(f"{base}^{exp}")
print("*".join(ans))