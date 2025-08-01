def palindrom1(s):
    d = [1 for i in range(len(s), 0, -1)]
    l = 0
    r = 0
    for i in range (1, len(s)):
        if (i < r):
            d[i] = min(r - i + 1, d[l + r - i])
        while (i - d[i] >= 0 and i + d[i] < len(s) and s[i - d[i]] == s[i + d[i]]):
            d[i] += 1
        if (i + d[i] - 1 > r):
            l = i - d[i] + 1
            r = i + d[i] - 1
    return d


def palindrom2(s):
    d = [0 for i in range(len(s), -1, -1)]
    l = -1
    r = -1
    for i in range (0, len(s) - 1):
        if (i < r):
            d[i] = min(r - i, d[l + r - i - 1])
        while (i - d[i] >= 0  and i + d[i] + 1 < len(s) and s[i - d[i]] == s[i + d[i] + 1]):
            d[i] += 1
        if (i + d[i] > r):
            l = i - d[i] + 1
            r = i + d[i]
    return d


s = input()
print(sum(palindrom2(s)) + sum(palindrom1(s)))