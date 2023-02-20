# 二分查找
"""
查找一个数组是局部最小索引
2 3 ....
.... 3 2
...  3 2 3 ...
上面3中形式都满足题意
"""


def bin_search3(li):
    n = len(li)
    if li[0] < li[1]:
        return 0

    elif li[-1] < li[-2]:
        return n - 1

    else:
        # \ .. .. /  一定是这种趋势，中间一定有局部最小
        left = 1
        right = n - 2
        while left < right:
            mid = left + ((right - left) >> 1)
            if li[mid] > li[mid-1]:
                right = mid - 1
            elif li[mid] > li[mid+1]:
                left = mid + 1
            else:
                return mid
        return left


if __name__ == '__main__':
    li = [53, 42, 33, 27, 13, 7, 34, 45, 65]
    ret = bin_search3(li)
    print(ret)
