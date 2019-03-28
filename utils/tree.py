'''
utils for tree
'''

class TreeNode(object):

    def __init__(self, item, left=None, right=None):
        self.item = item 
        self.left = left
        self.right = left


def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1
        

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

