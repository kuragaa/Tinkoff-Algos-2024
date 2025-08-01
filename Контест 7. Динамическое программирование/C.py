n, k = map(int, input().split())
cost = list(map(int, input().split()))
cost.append(0)
dp = [0] * (n + 1)
jumps = [-1] * (n + 1)

for i in range(2, n + 1):
    mx = float('-inf')
    prev = -1
    for j in range(1, min(i, k) + 1):
        if dp[i - j] > mx:
            mx = dp[i - j]
            prev = i - j
    dp[i] = cost[i - 2] + mx
    jumps[i] = prev

cur = n
ans = []
while cur != -1:
    ans.append(cur)
    cur = jumps[cur]
ans.reverse()

print(dp[n])
print(len(ans) - 1)
print(*ans)