import sys
sys.setrecursionlimit(10**6)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 1, 0, self.n - 1)

    def build_tree(self, arr, v, l, r):
        if l == r:
            self.tree[v] = arr[l]
        else:
            mid = (l + r) // 2
            self.build_tree(arr, 2 * v, l, mid)
            self.build_tree(arr, 2 * v + 1, mid + 1, r)
            self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1])

    def update(self, v, tl, tr, idx, new):
        if tl == tr:
            self.tree[v] = new
        else:
            mid = (tl + tr) // 2
            if idx <= mid:
                self.update(2 * v, tl, mid, idx, new)
            else:
                self.update(2 * v + 1, mid + 1, tr, idx, new)
            self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1])

    def x(self, v, tl, tr, l, r, x):
        if l > r:
            return float('inf')
        if tl == tr:
            if self.tree[v] >= x:
                return tl
            else:
                return float('inf')
        mid = (tl + tr) // 2
        if tl < l:
            return min(
                self.x(2 * v, tl, mid, l, min(r, mid), x),
                self.x(2 * v + 1, mid + 1, tr, max(l, mid + 1), r, x)
            )
        if self.tree[2 * v] < x:
            return self.x(2 * v + 1, mid + 1, tr, max(l, mid + 1), r, x)
        else:
            return self.x(2 * v, tl, mid, l, min(r, mid), x)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = SegmentTree(arr)
for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        tree.update(1, 0, n-1, op[1], op[2])
    else:
        ans = tree.x(1, 0, n-1, op[2], n-1, op[1])
        if ans == float('inf'):
            print(-1)
        else:
            print(ans)