def print_seq(dp, delete, s, i, j):
    if dp[i][j] == j - i + 1:
        pass
    elif dp[i][j] == 0:
        for k in range(i, j + 1):
            print(s[k], end='')
    elif delete[i][j] == -1:
        print(s[i], end='')
        print_seq(dp, delete, s, i + 1, j - 1)
        print(s[j], end='')
    else:
        print_seq(dp, delete, s, i, delete[i][j])
        print_seq(dp, delete, s, delete[i][j] + 1, j)

s = input()
n = len(s)

dp = [[0] * n for _ in range(n)]
delete = [[-1] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for j in range(n):
    for i in range(j - 1, -1, -1):
        if (s[i] == '(' and s[j] == ')') or (s[i] == '[' and s[j] == ']') or (s[i] == '{' and s[j] == '}'):
            mn = dp[i + 1][j - 1]
        else:
            mn = float('inf')
        p = -1
        for k in range(i, j):
            if dp[i][k] + dp[k + 1][j] < mn:
                mn = dp[i][k] + dp[k + 1][j]
                p = k
        dp[i][j] = mn
        delete[i][j] = p

print_seq(dp, delete, s, 0, n - 1)