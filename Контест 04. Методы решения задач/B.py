n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    sub = list(map(int, input().split()))
    arr.append(sub)
#print(arr)

psa = [[0] * m for _ in range(n)]
psa[0][0] = arr[0][0]

for i in range(1, n):
    psa[i][0] = psa[i - 1][0] + arr[i][0]

for i in range(1, m):
    psa[0][i] = psa[0][i - 1] + arr[0][i]

for i in range(1, n):
    for j in range(1, m):
        psa[i][j] = (psa[i - 1][j] +
                      psa[i][j - 1] -
                      psa[i - 1][j - 1] +
                      arr[i][j])

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    res = psa[y2-1][x2-1] - (psa[y2-1][x1-2] if x1-2 >=0 else 0) - (psa[y1-2][x2-1] if y1-2 >=0 else 0) + (psa[y1-2][x1-2] if x1-2 >=0 and y1-2 >=0 else 0)
    print(res)