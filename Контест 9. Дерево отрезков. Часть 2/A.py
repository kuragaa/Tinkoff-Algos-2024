import sys
sys.setrecursionlimit(100000)

class SegmentTree:
    def __init__(self, n):
        self.tree = [(0, 0) for _ in range(4 * n)]

    def update(self, v, tl, tr, l, r, val):
        if r < l or tl > tr or l > tr or r < tl:
            return
        if r == tr and l == tl:
            self.tree[v] = (self.tree[v][0], self.tree[v][1] + val)
        else:
            mid = (tl + tr) // 2
            self.update(2 * v, tl, mid, l, min(r, mid), val)
            self.update(2 * v + 1, mid + 1, tr, max(l, mid + 1), r, val)
            self.tree[v] = (min(self.tree[2 * v][0] + self.tree[2 * v][1], self.tree[2 * v + 1][0] + self.tree[2 * v + 1][1]), self.tree[v][1])

    def query(self, v, tl, tr, l, r):
        if l > r or tl > tr or l > tr or r < tl:
            return float('inf')
        add_v = self.tree[v][1]
        if r == tr and l == tl:
            return self.tree[v][0] + add_v
        mid = (tl + tr) // 2
        return min(self.query(2*v, tl, mid, l, min(r, mid)), self.query(2*v+1, mid+1, tr, max(l, mid+1), r)) + add_v


n, m = map(int, sys.stdin.readline().split())
tree = SegmentTree(n)
for _ in range(m):
    op = list(map(int, sys.stdin.readline().split()))
    if op[0] == 2:
        print(tree.query(1, 0, n - 1, op[1], op[2] - 1))
    else:
        tree.update(1, 0, n - 1, op[1], op[2] - 1, op[3])