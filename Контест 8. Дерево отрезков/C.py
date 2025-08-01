import sys
sys.setrecursionlimit(10**5)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 1, 0, self.n - 1)

    def build_tree(self, arr, v, l, r):
        if l == r:
            self.tree[v] = int(arr[l] == 1)
        else:
            mid = (l + r) // 2
            self.build_tree(arr, 2 * v, l, mid)
            self.build_tree(arr, 2 * v + 1, mid + 1, r)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def update(self, v, tl, tr, idx):
        if tl == tr:
            self.tree[v] = int(not bool(self.tree[v]))
        else:
            mid = (tl + tr) // 2
            if idx <= mid:
                self.update(2 * v, tl, mid, idx)
            else:
                self.update(2 * v + 1, mid + 1, tr, idx)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def k(self, v, tl, tr, k):
        if tl == tr:
            return tl
        mid = (tl + tr) // 2
        if k <= self.tree[2 * v]:
            return self.k(v*2, tl, mid, k)
        else:
            return self.k(v*2+1, mid+1, tr, k - self.tree[v*2])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = SegmentTree(arr)
for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        tree.update(1, 0, n-1, op[1])
    else:
        k = op[1] + 1
        print(tree.k(1, 0, n-1, k))