L, N = map(int, input().split())
marks = [0] + list(map(int, input().split())) + [L]
N += 2
dp = []
for i in range(N):
    dp.append([0] * N)

for j in range(1, N):
    for i in range(j - 2, -1, -1):
        dp[i][j] = float('inf')
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        dp[i][j] += marks[j] - marks[i]
print(dp[0][N - 1])
