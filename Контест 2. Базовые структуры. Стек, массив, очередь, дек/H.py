n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0]*(n+1)

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

left = [-1]*n
right = [n]*n
stack = []

for i in range(n):
    while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    stack.append(i)

stack.clear()

for i in range(n-1, -1, -1):
    while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    stack.append(i)

maxx = 0
for i in range(n):
    maxx = max(maxx, (prefix_sum[right[i]] - prefix_sum[left[i]+1]) * arr[i])

print(maxx)