import sys
import collections

def stack_op(arr, op):
    if op[0] == 1:
        if len(arr) == 0:
            arr.append(op[1])
        else:
            if arr[-1] < op[1]:
                arr.append(arr[-1])
            else:
                arr.append(op[1])
            #arr.append(min(arr[-1], op[1]))
    if op[0] == 2:
        arr.pop()
    if op[0] == 3:
        print(arr[-1])

arr = collections.deque()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    op = list(map(int, sys.stdin.readline().split()))
    stack_op(arr, op)