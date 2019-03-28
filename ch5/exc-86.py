'''
excercise 5.85
count leaf num of a tree
'''


def count_leaf(root):
    if not root:
        return None
    if not root.left and not root.right:
        return 1
    return count_leaf(root.left) + count(root.right)


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    assert count_leaf(tree) == 4
