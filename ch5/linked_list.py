#coding=utf-8
'''
single linked list methods using recursion
code 5.5
exc 5.14, 5.15
'''

class Node(object):
    def __init__(self, val):
        self.val = val 
        self.next = None


def count(head):
    if not head:
        return 0
    return 1 + count(head.next)


def traverse(head):
    r = []
    def _helper(n):
        if not n:
            return
        r.append(n.val)
        _helper(n.next)
    _helper(head)
    return r


def traverseR(head):
    r = []
    def _helper(n):
        if not n:
            return
        _helper(n.next)
        r.append(n.val)
    _helper(head)
    return r


def delete(head, val):
    if not head:
        return None
    if head.val == val:
        return head.next
    head.next = delete(head.next, val)
    return head


def delete_last(head):
    if not head or not head.next:
        return
    if not head.next.next:
        head.next = None
        return
    delete_last(head.next)


def reverse(head):
    dummy = Node(None)
    tmp = [dummy, ]
    def _r(node):
        if not node:
            return None
        _r(node.next)
        tmp[0].next = node
        tmp[0] = tmp[0].next
        node.next = None
    _r(head)
    return dummy.next


if __name__ == '__main__':
    head = t = Node(0)
    for i in range(1, 10):
        t.next = Node(i)
        t = t.next
    assert count(head) == 10
    assert tuple(traverse(head)) == tuple(range(10))
    assert tuple(traverseR(head)) == tuple(range(9, -1, -1))

    head = delete(head, 50)
    assert count(head) == 10
    head = delete(head, 5)
    assert count(head) == 9
    assert 5 not in traverse(head)

    delete_last(head)
    assert count(head) == 8

    print traverse(head)
    head = reverse(head)
    print traverse(head)
