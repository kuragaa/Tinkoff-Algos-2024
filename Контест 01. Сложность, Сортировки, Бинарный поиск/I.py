def change(a, i):
    a[i-1] = 1

n = int(input())
ind = [int(i) for i in input().split()]
a = [0]*n
end = n-1
ones_end = 0
for i in range(n):
    print(i - ones_end + 1, end=' ')
    change(a, ind[i])
    while end > -1 and a[end] != 0:
        ones_end += 1
        end -= 1
print(1)