from collections import deque

def mins(arr, k):
    q = deque()
    mins = []
    for i in range(len(arr)):
        if len(q) > 0 and q[0] <= i - k:
            q.popleft()  
        while len(q) > 0 and arr[q[-1]] >= arr[i]:
            q.pop()  
        q.append(i)
        if i >= k-1:
            mins.append(arr[q[0]])  
    return mins

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = mins(arr, k)
print(*res)