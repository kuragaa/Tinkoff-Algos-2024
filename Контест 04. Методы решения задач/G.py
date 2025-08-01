n = int(input())
office = []
cnt = 0
for _ in range(n):
    time = list(map(int, input().split()))
    start = time[0] * 60 * 60 + time[1] * 60 + time[2]
    end = time[3] * 60 * 60 + time[4] * 60 + time[5]
    if start == end:
        cnt += 1
    elif start > end and end != 0:
        office.append((0, 1))
        office.append((end, -1))
        office.append((start, 1))
    elif end == 0:
        office.append((start, 1))
        office.append((86400, -1))
    else:
        office.append((start, 1))
        office.append((end, -1))

if not office:
    print(86400)
    exit()
office.sort(key=lambda x: x[0])

#print(office)

start = -1
end = -1
c = 0
k = 0
ans = 0
for pair in office:
    c += pair[1]
    if c >= n-cnt:
        if k < 1:
            start = pair[0]
            k += 1
    else:
        if start != -1:
            end = pair[0]

    if start != -1 and end != -1:
        ans = ans + (end-start)
        k = 0
        start = -1
        end = -1

if start != -1:
    ans = ans + (86400 - start)

print(ans)