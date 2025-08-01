n = int(input())
arr = list(map(int, input().split()))
ps = [0]*(n+1)
x = [0]*(n+1)
for i in range(1, len(ps)):
    ps[i] = ps[i-1] + arr[i-1]
    x[i] = x[i - 1] ^ arr[i - 1]

m = int(input())
for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        print(ps[op[2]]-ps[op[1]-1])
    elif op[0] == 2:
        print(x[op[2]]^x[op[1]-1])