s = input()
n = len(s)
dp = [[''] * n for _ in range(n)]
for l in range(1, n+1):
    for start in range(n - l + 1):
        end = start + l - 1
        subs = s[start:end + 1]
        min_subs = subs
        if l > 4:
            for end2 in range(start, end):
                start2 = end2 + 1
                temp = dp[start][end2] + dp[start2][end]
                if len(min_subs) > len(temp):
                    min_subs = temp
            for k in range(1, l):
                if l % k == 0:
                    flag = True
                    for i in range(start + k, end + 1):
                        if s[i] != s[i - k]:
                            flag = False
                            break
                    if flag:
                        temp = str(l // k) + '(' + dp[start][start + k - 1] + ')'
                        if len(temp) < len(min_subs):
                            min_subs = temp
        dp[start][end] = min_subs
print(dp[0][n - 1])