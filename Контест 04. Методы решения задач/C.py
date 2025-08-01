n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = arr[-1] - arr[0] + 1
while left < right:
    gap = (left + right) // 2
    cows = 1
    last = arr[0]
    for stall in arr:
        if stall - last > gap:
            cows += 1
            last = stall
    if cows >= k:
        left = gap + 1
    else:
        right = gap
print(left)