'''
exercise 5.88
internal path of a tree
'''
from utils.tree import TreeNode as Node


def internal_path(root):
    r = [0,]
    def _helper(node, level):
        if not node or is_leaf(node):
            return
        r[0] += level
        _helper(node.left, level + 1)
        _helper(node.right, level + 1)
    _helper(root, 0)
    return r[0]


def is_leaf(node):
    return bool(not node.left and not node.right)


def internal_path_2(root):
    return _internal_path(root, 0)


def _internal_path(node, level):
    if not node or is_leaf(node):
        return 0
    return (_internal_path(node.left, level + 1)
            + _internal_path(node.right, level + 1)
            +  level)


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(2)
    tree.right.right = Node(2)
    tree.left.left = Node(3)
    tree.left.left.left = Node(3)
    tree.left.right = Node(3)
    tree.left.right.right = Node(3)

    assert internal_path(tree) == internal_path_2(tree)

