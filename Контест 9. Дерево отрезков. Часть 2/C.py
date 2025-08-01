import sys
sys.setrecursionlimit(10000)

class SegmentTree:
    class Node:
        def __init__(self, left, right):
            self.num = 0
            self.ttl_bl = 0
            self.flag = False
            self.updated = False
            self.left = left
            self.right = right

    def __init__(self, n):
        self.tree = [None] * (4 * n)
        self.build(1, 0, n-1)

    def build(self, v, tl, tr):
        self.tree[v] = self.Node(tl, tr)
        if tr != tl:
            mid = (tl + tr) // 2
            self.build(2*v+1, mid+1, tr)
            self.build(2*v, tl, mid)

    def update_tr(self, v):
        if not self.tree[v].updated:
            return
        if self.tree[v].flag:
            self.tree[v].ttl_bl = 1
            self.tree[v].num = self.tree[v].right - self.tree[v].left + 1
        else:
            self.tree[v].ttl_bl = self.tree[v].num = 0
        self.tree[v].updated = False

        if self.tree[v].right == self.tree[v].left:
            return
        self.tree[2*v].updated = self.tree[2*v+1].updated = True
        self.tree[2*v].flag = self.tree[2*v+1].flag = self.tree[v].flag

    def update_seg(self, v, val, l, r):
        if self.tree[v].left > r or self.tree[v].right < l:
            return
        if self.tree[v].left >= l and self.tree[v].right <= r:
            self.update_tr(v)
            self.tree[v].updated = True
            self.tree[v].flag = val
            return
        self.update_tr(v)
        self.update_seg(2*v+1, val, l, r)
        self.update_seg(2*v, val, l, r)

        seg = 2*v+1
        while True:
            self.update_tr(seg)
            if self.tree[seg].right == self.tree[seg].left:
                break
            seg = 2*seg
        right = True if self.tree[seg].num == 1 else False

        seg = 2*v
        while True:
            self.update_tr(seg)
            if self.tree[seg].right == self.tree[seg].left:
                break
            seg = 2*seg+1
        left = True if self.tree[seg].num == 1 else False

        self.tree[v].ttl_bl = self.tree[2*v+1].ttl_bl + self.tree[2*v].ttl_bl
        self.tree[v].num = self.tree[2 * v + 1].num + self.tree[2 * v].num
        if left and right:
            self.tree[v].ttl_bl -=1

n = int(input())
stree = SegmentTree(1000001)
for _ in range(n):
    op = input().split()
    l = int(op[2])
    x = int(op[1])
    if l > 0:
        l -= 1
    else:
        l += 1
    stree.update_seg(1, (op[0] == 'B'), x + 500_000, x + l + 500_000)
    print(stree.tree[1].ttl_bl, stree.tree[1].num)