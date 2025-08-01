def longest(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def palindrom(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and l != 2:
                dp[i][j] = dp[i + 1][j - 1] + 2
            elif s[i] == s[j] and l == 2:
                dp[i][j] = 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    i, j = 0, n - 1
    res = ""
    while i < j:
        if s[i] == s[j]:
            res += s[i]
            i += 1
            j -= 1
        elif dp[i + 1][j] > dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    mid = ""
    if i == j:
        mid = s[i]

    return res + mid + res[::-1]


s = input().strip()
print(longest(s))
print(palindrom(s))