from math import gcd
import sys

n, k = map(int, sys.stdin.readline().split())
res = (n // gcd(n,k)) * k
print(res)