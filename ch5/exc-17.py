#coding=utf-8
'''
max item of a linked list 
'''

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None 


def max_item(head):
    if not head:
        return 0
    if not head.next:
        return head.item
    return max(head.item, max_item(head.next))


if __name__ == '__main__':
    head = tmp = Node(0)
    for i in range(10):
        tmp.next = Node(i) 
        tmp = tmp.next
    assert max_item(head) == 9
