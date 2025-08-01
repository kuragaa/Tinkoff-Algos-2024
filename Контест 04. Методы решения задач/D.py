def count(x, n):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)
    return count


def search(n, k):
    left = 1
    right = n*n
    while left < right:
        mid = (left + right) // 2
        if count(mid, n) < k:
            left = mid + 1
        else:
            right = mid
    return left


n, k = map(int, input().split())
print(search(n, k))