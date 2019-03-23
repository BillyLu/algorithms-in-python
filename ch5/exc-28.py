#coding=utf-8
'''
tailing 0 numbers of a binary num
'''

def tailing_zeros(num):
    if num == 0:
        return 1
    if num & 1 == 1:
        return 0
    return 1 + tailing_zeros(num >> 1)



if __name__ == '__main__':
    assert tailing_zeros(0) == 1
    assert tailing_zeros(1) == 0
    assert tailing_zeros(2) == 1
    assert tailing_zeros(36) == 2
