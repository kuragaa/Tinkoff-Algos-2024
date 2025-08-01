from math import *

def check(x):
    return x**2 + sqrt(x+1)

def binary(c):
    l = 0
    r = c
    eps = 0.000001
    while r - l > eps:
        mid = (l+r) / 2
        if check(mid) - c > 0:
            r = mid
        else:
            l = mid
    return mid

c = float(input())
print(binary(c))