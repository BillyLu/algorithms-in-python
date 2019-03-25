# coding=utf-8
'''
code 5.13
'''

SIZE, VAL = 0, 1

def knap(items, cap):
    memo, pack = {}, {}
    max_val = _knap(items, cap, memo, pack)
    print_pack(pack, cap)
    return max_val


def _knap(items, cap, memo, pack):
    if memo.get(cap):
        return memo[cap] 
    max_val = max_index = 0
    for i, item in enumerate(items):
        left = cap - item[SIZE]
        if left >= 0:
            val = item[VAL] + _knap(items, left, memo, pack)
            if val > max_val:
                max_val = val
                max_index = i
    memo[cap], pack[cap] = max_val, items[max_index]
    return max_val


def print_pack(pack, cap):
    '''print current pack detail'''
    r = []
    while cap:
        item = pack[cap]
        r.append(item)
        cap -= item[SIZE]
    print r    

if __name__ == '__main__':
    items = [
            [3, 4],
            [4, 5],
            [7, 10],
            [8, 11],
            [9, 13],
            ]
    cap = 17
    assert knap(items, cap) == 20
