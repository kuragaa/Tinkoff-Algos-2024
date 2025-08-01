import sys
from collections import deque

def queue(arr, q, id, k):
    if arr[0] == 1:
        id[arr[1]] = len(q) + k
        q.append(arr[1])
    elif arr[0] == 2:
        q.popleft()
        k += 1
    elif arr[0] == 3:
        q.pop()
    elif arr[0] == 4:
        print(id[arr[1]] - k)
    elif arr[0] == 5:
        print(q[0])
    return k

n = int(sys.stdin.readline().strip())
q = deque()
id = {}
k = 0
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    k = queue(arr, q, id, k)