n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

if n == 1 and m == 1:
    print(1)
    print(1, 1)
    exit()

dp = [[0]*m for _ in range(n)]
x, y, mx = 0, 0, 0
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] > 0:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
        if dp[i][j] > mx:
            mx = dp[i][j]
            x = i - mx + 1
            y = j - mx + 1

print(mx)
print(x+1, y+1)