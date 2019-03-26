'''
tree  traverse
'''
from collections import deque

class Node(object):
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left 
        self.right = right


def preorder_rec(root):
    r = []
    def _helper(node):
        if not node:
            return 
        r.append(node.item)
        _helper(node.left)
        _helper(node.right)
    _helper(root)
    return r


def preorder_iter(root):
    if not root:
        return []
    r, stack = [], deque([root, ])
    while stack:
        node = stack.pop()
        r.append(node.item)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return r


def inorder_iter(root):
    if not root:
        return []
    r, seen, stack = [], set(), deque([root, ]) 
    while stack:
        node = stack.pop()
        if node in seen:
            r.append(node.item)
            continue
        if node.right:
            stack.append(node.right)
        stack.append(node)
        if node.left:
            stack.append(node.left)
        seen.add(node)
    return r    


def postorder_iter(root):
    if not root:
        return []
    r, seen, stack = [], set(), deque([root, ])
    while stack:
        node = stack.pop()
        if node in seen:
            r.append(node.item)
            continue
        stack.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        seen.add(node)
    return r   


def level_traverse(root):
    if not root:
        return []
    r, queue = [], deque([root, ])
    while queue:
        node = queue.popleft()
        r.append(node.item)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return r


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    preorder = (1, 2, 4, 5, 3, 6, 7)
    inorder = (4, 2, 5, 1, 6, 3, 7)
    postorder = (4, 5, 2, 6, 7, 3, 1)
    leverorder = (1,2,3,4,5,6,7)
    assert tuple(preorder_rec(tree)) == preorder
    assert tuple(preorder_iter(tree)) == preorder
    assert tuple(level_traverse(tree)) == leverorder 
    assert tuple(inorder_iter(tree)) == inorder 
    assert tuple(postorder_iter(tree)) == postorder 

