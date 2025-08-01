import sys

sys.setrecursionlimit(10**5+7000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def new_node(d):
    return Node(d)


def maximum(x, y):
    return x if x >= y else y


def height(node):
    if node is None:
        return 0
    return 1 + maximum(height(node.left), height(node.right))


def is_bst(node, min_val, max_val):
    if node is None:
        return True
    if node.val <= min_val or node.val >= max_val:
        return False
    return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)

def is_avl(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) <= 1 and is_avl(root.left) and is_avl(root.right) and is_bst(root.left, float("-inf"), root.val) and is_bst(root.right, root.val, float("inf")):
        return True
    return False

n, root_val = map(int, input().split())
nodes = [None] * n
for i in range(n):
    nodes[i] = new_node(i)
for i in range(n):
    left_child, right_child = map(int, input().split())
    if left_child != -1:
        nodes[i].left = nodes[left_child]
    if right_child != -1:
        nodes[i].right = nodes[right_child]

root3 = nodes[root_val]

if is_avl(root3):
    print(1)
else:
    print(0)