def check(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d


def binary():
    r = 1
    while check(r, a, b, c, d) * check(-r, a, b, c, d) >= 0:
        r *= 2
    l = -r
    eps = 0.000001
    while r - l > eps:
        mid = (l+r) / 2
        if check(mid, a, b, c, d)*check(r, a, b, c, d) > 0:
            r = mid
        else:
            l = mid
    return mid

a, b, c, d = map(int, input().split())
print(binary())