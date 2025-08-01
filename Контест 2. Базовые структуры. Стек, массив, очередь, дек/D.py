n = int(input())
arr = list(map(int, input().split()))
q = []
prev = arr[0]
cnt = 0
res = 0
for i in range(n):
    if arr[i] == prev:
        cnt += 1
        q.append([arr[i], cnt])
    else:
        if cnt >= 3:
            res += cnt
            for _ in range(cnt):
                q.pop()
            if arr[i] == q[-1][0]:
                cnt = q[-1][1] + 1
            else:
                cnt = 1
            prev = arr[i]
            q.append([arr[i], cnt])
        else:
            cnt = 1
            prev = arr[i]
            q.append([arr[i], cnt])
if cnt >= 3:
    res += cnt
print(res)