import sys
from collections import deque

def queue(op, left, right):

    if op[0] == '+':
        left.appendleft(int(op[1]))

    elif op[0] == '*':
        while len(left) > len(right):
            right.appendleft(left.pop())
        left.append(int(op[1]))

    elif op[0] == '-':
        while len(left) > len(right):
            right.appendleft(left.pop())
        print(right.pop())

n = int(sys.stdin.readline().strip())
op = []
left = deque()
right = deque()
for _ in range(n):
    op = list(sys.stdin.readline().split())
    queue(op, left, right)