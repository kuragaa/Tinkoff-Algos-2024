from collections import deque
n = int(input())
a = [int(i) for i in input().split()]
deq = deque()
maxim = float("-inf")
for i in enumerate(a):
    if len(deq) == 0:
        deq.append(i)
    elif i[1] >= deq[len(deq) - 1][1]:
        deq.append(i)
    else:
        while len(deq) > 0 and deq[len(deq) - 1][1] > i[1]:
            x = deq.pop()
            if len(deq) > 0:
                maxim = max(x[1] * (i[0] - deq[len(deq) - 1][0] - 1), maxim)
            else:
                maxim = max(x[1] * i[0], maxim)
        deq.append(i)
while len(deq) > 0:
    x = deq.pop()
    if len(deq) > 0:
        maxim = max(x[1] * (n - deq[len(deq) - 1][0] - 1), maxim)
    else:
        maxim = max(n * x[1], maxim)
print(maxim)