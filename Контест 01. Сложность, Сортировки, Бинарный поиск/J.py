import sys

def arifm(a1, an, n):
    return (a1+an) / 2 * n

def sum_v(z, n, m):
    p1 = arifm(1, (z-1)+(n-1)*m, (z-1)*n)
    p2 = arifm(z, m*n, (m-z+1)*n)
    return p1, p2, int(abs(p2 - p1))

def sum_h(z, n, m):
    z_el = 1 + (z - 1) * m
    p1 = arifm(1, (z-1)*m, (z-1)*m)
    p2 = arifm(z_el, n*m, n*m - z_el + 1)
    return p1, p2, int(abs(p2 - p1))

def binary_search_V(n, m):
    left, right = 1, m
    best_diff = float('inf')
    best_ind = -1

    while left <= right:
        mid = (left + right) // 2
        p1, p2, current_diff = sum_v(mid, n, m)

        if current_diff < best_diff:
            best_diff = current_diff
            best_ind = mid

        if p1 > p2:
            right = mid - 1
        else:
            left = mid + 1
    return best_diff, best_ind

def binary_search_H(n, m):
    left, right = 1, n
    best_diff = float('inf')
    best_ind = -1

    while left <= right:
        mid = (left + right) // 2
        p1, p2, current_diff = sum_h(mid, n, m)

        if current_diff < best_diff:
            best_diff = current_diff
            best_ind = mid

        if p1 > p2:
            right = mid - 1
        else:
            left = mid + 1
    return best_diff, best_ind

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = (map(int, sys.stdin.readline().split()))
    if n == 1:
        sum, res = binary_search_V(n, m)
        print('V', res)
    elif m == 1:
        sum, res = binary_search_H(n, m)
        print('H', res)
    else:
        sum1, res1 = binary_search_V(n, m)
        sum2, res2 = binary_search_H(n, m)
        if sum1 < sum2:
            print('V', res1)
        elif sum1 == sum2:
            print('V', res1)
        elif sum1 > sum2:
            print('H', res2)