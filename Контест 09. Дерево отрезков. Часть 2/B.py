class Node:
    def __init__(self):
        self.assign = -1
        self.add = 0
        self.ttl = 0

class SegmentTree:
    def __init__(self, n):
        self.tree = [Node() for _ in range(4 * n)]

    def update(self, v, s):
        if self.tree[v].assign != -1:
            if s != 1:
                self.tree[2*v].add = self.tree[2*v+1].add = 0
                self.tree[2*v].assign = self.tree[2*v+1].assign = self.tree[v].assign
            self.tree[v].ttl = self.tree[v].assign * s
        self.tree[v].assign = -1
        if s != 1:
            self.tree[2*v+1].add += self.tree[v].add
            self.tree[2*v].add += self.tree[v].add
        self.tree[v].ttl += self.tree[v].add * s
        self.tree[v].add = 0

    def do_assign(self, v, tl, tr, l, r, val):
        self.update(v, tr - tl + 1)
        if r < l:
            return
        if r == tr and l == tl:
            self.tree[v].add = 0
            self.tree[v].assign = val
            self.update(v, tr - tl + 1)
        else:
            mid = (tl + tr) // 2
            self.do_assign(2*v+1, mid+1, tr, max(l, mid+1), r, val)
            self.do_assign(2*v, tl, mid, l, min(r, mid), val)
            self.tree[v].ttl = self.tree[2*v+1].ttl + self.tree[2*v].ttl

    def add_val(self, v, tl, tr, l, r, val):
        self.update(v, tr - tl + 1)
        if r < l:
            return
        if r == tr and l == tl:
            self.tree[v].add += val
            self.update(v, tr - tl + 1)
        else:
            mid = (tl + tr) // 2
            self.add_val(2 * v + 1, mid + 1, tr, max(l, mid + 1), r, val)
            self.add_val(2 * v, tl, mid, l, min(r, mid), val)
            self.tree[v].ttl = self.tree[2 * v + 1].ttl + self.tree[2 * v].ttl

    def find_ttl(self, v, tl, tr, l, r):
        self.update(v, tr - tl + 1)
        if r == tr and l == tl:
            return self.tree[v].ttl
        if r < l:
            return 0
        mid = (tl + tr) // 2
        return self.find_ttl(2*v+1, mid+1, tr, max(l, mid+1), r) + self.find_ttl(2*v, tl, mid, l, min(r, mid))

n, m = map(int, input().split())
tree = SegmentTree(n)
for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        tree.do_assign(1, 0, n-1, op[1], op[2]-1, op[3])
    elif op[0] == 2:
        tree.add_val(1, 0, n-1, op[1], op[2]-1, op[3])
    else:
        print(tree.find_ttl(1, 0, n-1, op[1], op[2]-1))