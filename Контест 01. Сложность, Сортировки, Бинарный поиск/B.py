def binary_search(arr, key):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) // 2
        guess = arr[mid]
        if guess == key:
            return guess
        elif guess > key:
            r = mid
        else:
            l = mid + 1
    if l > 0 and abs(arr[l-1] - key) <= abs(arr[l] - key):
        return arr[l-1]
    else:
        return arr[l]

n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
# arr = list(map(int, input().split()))
keys = [int(i) for i in input().split()]
# keys = list(map(int, input().split()))

for i in range(k):
    print(binary_search(arr, keys[i]))