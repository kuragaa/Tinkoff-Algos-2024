n = int(input())
dp = [1, 1, 1]
for i in range(n-1):
    prev = [sum(dp[1:3]), sum(dp), sum(dp)]
    dp = prev
print(sum(dp))
