n = int(input())
arr = list(map(int, input().split()))
n = len(arr)
dp = [1] * n
idx = [-1] * n

for i in range(n):
    mx_len = 0
    prev = i
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > mx_len:
            mx_len = dp[j]
            prev = j
    dp[i] = mx_len + 1
    idx[i] = prev

cur = max(range(n), key=lambda x: dp[x])
print(dp[cur])

seq = [arr[cur]]
while cur != idx[cur]:
    cur = idx[cur]
    seq.append(arr[cur])
seq.reverse()
print(*seq)