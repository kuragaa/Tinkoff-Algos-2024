import sys
sys.setrecursionlimit(10**5)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [(0, 0)] * (4 * self.n)
        self.build_tree(arr, 0, 0, self.n - 1)

    def build_tree(self, arr, v, l, r):
        if l == r:
            self.tree[v] = (arr[l], 1)
        else:
            mid = (l + r) // 2
            self.build_tree(arr, 2 * v + 1, l, mid)
            self.build_tree(arr, 2 * v + 2, mid + 1, r)
            self.tree[v] = self.combine(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def update(self, v, tl, tr, idx, new):
        if tl == tr:
            self.tree[v] = (new, 1)
        else:
            mid = (tl + tr) // 2
            if idx <= mid:
                self.update(2 * v + 1, tl, mid, idx, new)
            else:
                self.update(2 * v + 2, mid + 1, tr, idx, new)
            self.tree[v] = self.combine(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return (float('inf'), 0)
        if l == tl and r == tr:
            return self.tree[v]
        mid = (tl + tr) // 2
        return self.combine(
            self.query(2 * v + 1, tl, mid, l, min(r, mid)),
            self.query(2 * v + 2, mid + 1, tr, max(l, mid + 1), r)
        )

    def combine(self, a, b):
        if a[0] < b[0]:
            return a
        elif a[0] > b[0]:
            return b
        else:
            return (a[0], a[1] + b[1])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = SegmentTree(arr)
for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 2:
        result = tree.query(0, 0, tree.n - 1, op[1], op[2] - 1)
        print(result[0], result[1])
    else:
        tree.update(0, 0, tree.n - 1, op[1], op[2])