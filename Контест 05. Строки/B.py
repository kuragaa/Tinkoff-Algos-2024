def prefix(s):
    n = len(s)
    p = [0] * n

    for i in range(1, n):
        j = p[i - 1]
        while j > 0 and s[i] != s[j]:
            j = p[j - 1]
        if s[i] == s[j]:
            j += 1
        p[i] = j

    return p


def find(s, sub):
    idx = []
    p = prefix(sub + '#' + s)
    n = len(s)
    m = len(sub)
    #print(p)

    for i in range(m + 1, n + 1 + m):
        if p[i] == m:
            idx.append(i - 2 * m)

    return idx


s = input()
n = int(input())
for _ in range(n):
    sub = input()
    ans = find(s, sub)
    print(len(ans), *ans)