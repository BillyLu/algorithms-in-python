#coding=utf-8
'''
max item of a array
'''

def max_item(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], max_item(nums[1:]))


if __name__ == '__main__':
    n = range(10)
    assert max_item(n) == 9

    n = range(10)[::-1]
    assert max_item(n) == 9
