'''
tree alg
'''
from random import shuffle
from collections import deque


class Node(object):
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def count(root):
    if not root:
        return 0
    return count(root.left) + count(root.right) + 1


def height(root):
    if not root:
        return 0
    left_tree = height(root.left)
    right_tree = height(root.right)
    return max(left_tree, right_tree) + 1
        

def tournament(teams):
    def _helper(l, r):
        if l > r:
            return None
        m = (l + r) / 2
        node = Node(teams[m])
        if l == r:
            return node
        node.left = _helper(l, m)
        node.right = _helper(m + 1, r)
        node.item = max(node.left.item, node.right.item)
        return node
    return _helper(0, len(teams) - 1)


def show(root, h=0):
    if not root:
        _print('*', h)
        return
    show(root.left, h + 1)
    _print(root.item, h)
    show(root.right, h + 1)


def _print(item, h):
    print ' ' * h, item


def print_tree(root):
    if not root:
        return
    h = height(root)
    level_nodes = [' ' for _ in range(2 ** h - 1)]
    nodes = [level_nodes[:] for _ in range(h) ]
    def _printer(node, level, l, r):
        if not node:
            return
        m = (l + r) / 2
        nodes[level][m] = str(node.item)
        if node.left:
            _printer(node.left, level + 1, l, m)
        if node.right:
            _printer(node.right, level + 1, m, r)
    _printer(root, 0, 0, len(level_nodes))
    for n in nodes:
        print ' '.join(n)



if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    print_tree(tree)
    show(tree)
    assert count(tree) == 7
    assert height(tree) == 3
    teams = range(32)
    shuffle(teams)
    print_tree(tournament(teams))
