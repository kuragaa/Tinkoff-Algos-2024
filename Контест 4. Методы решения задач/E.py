def sections(arr, s):
    sections = 0
    cur_s = 0

    for i in range(len(arr)):
        if cur_s + arr[i] > s:
            cur_s = 0
            sections += 1
        if arr[i] > s:
            return float('inf')
        cur_s += arr[i]
    if cur_s:
        sections += 1

    return sections

n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = max(arr)
right = sum(arr)

while left < right:
    mid = (left + right) // 2
    if sections(arr, mid) <= k:
        right = mid
    else:
        left = mid + 1

print(left)