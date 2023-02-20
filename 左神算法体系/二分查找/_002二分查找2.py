# 二分查找
# 找到 >= x 最左侧的位置


def bin_search2(li, k):
    n = len(li)
    l = 0
    r = n - 1
    target = -1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if li[mid] > k:
            r = mid - 1
        elif li[mid] < k:
            l = mid + 1
        else:
            target = mid
            r = mid - 1
    return target

# 找到 <= x 最右侧的位置
# 1 1 2 2 3 3 _3_ 4 4 4
def bin_search3(li, k):
    n = len(li)
    l = 0
    r = n - 1
    target = -1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if li[mid] > k:
            r = mid - 1
        elif li[mid] < k:
            l = mid + 1
        else:
            target = mid
            l = mid + 1
    return target


if __name__ == '__main__':
    li = [1, 2, 3, 3, 3, 37, 34, 45, 65]
    ret = bin_search2(li, 3)
    print(ret)

    li = [1, 2, 3, 3, 3, 37, 39, 45, 65]
    ret = bin_search3(li, 3)
    print(ret)
