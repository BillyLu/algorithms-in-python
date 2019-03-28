'''
exercise 5.91
remove a team from a tournament
'''
from utils.tree import TreeNode, print_tree


def remove(root, item):
    if not root:
        return None
    if root.item == item:
        if not root.left and not root.right:
            return None
        if root.left.item != item:
            root.item =  root.left.item
        else:
            root.item =  root.right.item
    root.left = remove(root.left, item)
    root.right = remove(root.right, item)
    return root


if __name__ == '__main__':
    t = TreeNode(10)
    t.left = TreeNode(9)
    t.right = TreeNode(10)
    t.left.left = TreeNode(9)
    t.left.left.left = TreeNode(9)
    t.left.left.right = TreeNode(2)
    t.left.right = TreeNode(1)
    print_tree(t)
    t = remove(t, 9)
    print_tree(t)
    
