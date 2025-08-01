import sys
import time


class Pos:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

def x_sum(idx):
    ttl = 0
    while idx >= 0:
        a = x_arr[idx]
        ttl += a
        idx = (idx & (idx + 1)) - 1
    return ttl

def add_to_x(idx, add):
    while idx < len(x_arr):
        x_arr[idx] += add
        idx |= idx + 1

def add_x_range(start, end, add):
    if start > -1:
        add_to_x(start, add)
    if end > -1:
        add_to_x(end, -add)


inp = list(map(int, sys.stdin.readline().split()))
n = inp[2]
sectors = []
for i in range(n):
    x, y = map(float, input().split())
    sectors.append(Pos(int(x * 2), int(y * 2), i))

y_arr = []
for s in sectors:
    y_arr.append(s.y)
y_arr = sorted(set([s.y for s in sectors]))
sectors.sort(key=lambda s: s.x)

x_arr = [0]*len(y_arr)
res = [0]*n
for s in sectors:
    y_idx = y_arr.index(s.y)
    dist = s.x - x_sum(y_idx)
    res[s.num] = dist
    start = next((i for i, v in enumerate(y_arr) if v > s.y - dist), -1)
    end = next((i for i, v in enumerate(y_arr) if v > s.y + dist), -1)
    add_x_range(start, end, dist * 2)

sys.stdout.write(' '.join(map(str, res)))