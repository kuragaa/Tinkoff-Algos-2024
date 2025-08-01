s = input()
t = input()
n, m = len(s), len(t)
dp = [[0]*(m + 1) for i in range(n + 1)]

for i in range(n+1):
    for j in range(m+1):
        if min(i, j) == 0:
            dp[i][j] = max(i, j)
        else:
            in_s = dp[i - 1][j] + 1
            in_t = dp[i][j - 1] + 1
            rep = dp[i - 1][j - 1] + (s[i - 1] != t[j - 1])
            dp[i][j] = min(in_s, in_t, rep)
            if i > 1 and j > 1 and s[i - 2] == t[j - 1] and s[i - 1] == t[j - 2]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

print(dp[n][m])