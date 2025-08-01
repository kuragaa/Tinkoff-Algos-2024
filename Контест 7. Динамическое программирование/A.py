n = int(input())
cost = list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = cost[0]
for i in range(2, n+1):
    dp[i] = cost[i-1] + min(dp[i-1], dp[i-2])
print(dp[-1])