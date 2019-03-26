'''
exercise 5.84
given a tree's in-order and pre-order traverse as input
return level-order traverse
'''
from collections import deque


class TreeNode(object):
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left 
        self.right = right 


def gen_level_order(inorder, preorder):
    return _level_order_traverse(_build_tree(inorder, preorder))


def _build_tree(inorder, preorder):
    if not inorder or not preorder:
        return None
    node = TreeNode(preorder.pop(0)) 
    index = inorder.index(node.item)
    node.left = _build_tree(inorder[:index], preorder)
    node.right = _build_tree(inorder[index + 1:], preorder)
    return node


def _level_order_traverse(root):
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
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    levelorder = [1,2,3,4,5,6,7]
    assert tuple(gen_level_order(inorder, preorder)) == tuple(levelorder)
