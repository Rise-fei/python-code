l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(li, val):
    left = 0
    right = len(li) - 1

    while left <= right:
        # mid = (left + right) // 2
        # python 中不会溢出 但是java可能会溢出int32
        mid = left + ((right - left) >> 1)
        if li[mid] < val:
            left = mid + 1
        elif li[mid] > val:
            right = mid - 1
        else:
            return mid
    else:
        return None


def binary_search2(li, val):
    """
    1111111111222233333
    找到最左边的2
    """

    left = 0
    right = len(li) - 1
    left_index = -1

    while left <= right:
        # mid = (left + right) // 2
        # python 中不会溢出 但是java可能会溢出int32
        mid = left + ((right - left) >> 1)
        if li[mid] >= val:
            left_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return left_index


ret = binary_search(l, 5)
print(ret)
l2 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
ret = binary_search2(l2, 5)
print(ret)



"""
局部最小：
给定一个无序数组， 任意相邻的两个数不相等， 找出任意一个局部最小
二分实现：  
"""
def func(l):
    n = len(l)
    if l[0] < l[1]:
        return l[0]
    if l[n-1] <l[n-2]:
        return l[n-1]

    left = 0
    right = n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if l[mid] > l[mid] - 1:
            right = mid - 1
        elif l[mid] > l[mid] + 1:
            left = mid + 1
        else:
            return mid
    return left
