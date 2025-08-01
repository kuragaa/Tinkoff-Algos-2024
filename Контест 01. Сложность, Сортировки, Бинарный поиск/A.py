def binary_search(arr, key):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        guess = arr[mid]
        if guess == key:
            return 'YES'
        elif guess > key:
            r = mid - 1
        else:
            l = mid + 1
    return 'NO'

n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
keys = [int(i) for i in input().split()]

for i in range(k):
    print(binary_search(arr, keys[i]))
