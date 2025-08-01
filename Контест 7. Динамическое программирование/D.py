def paths(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return 0
    if dp[x][y] == -1:
        dp[x][y] = paths(x-1, y-2) + paths(x+1, y-2) + paths(x-2, y+1) + paths(x-2, y-1)
    return dp[x][y]

n, m = map(int, input().split())
dp = [[-1]*m for i in range(n)]
dp[0][0] = 1
print(paths(n-1, m-1))