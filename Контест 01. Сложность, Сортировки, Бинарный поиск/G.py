def antiq(n, a):
    if n == 1:
        a[0] = 1
        return
    if n == 2:
        a[0], a[1] = 1, 2
        return
    else:
        a[0], a[1] = 1, 2
        i = 2
        for k in range(3, n+1):
            a[i] = k
            a[(i)//2], a[i] = a[i], a[(i)//2]
            i += 1

n = int(input())
a = [0]*n
antiq(n, a)
print(*a)