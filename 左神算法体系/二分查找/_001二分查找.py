# 二分查找


def bin_search(li, k):
    n = len(li)
    l = 0
    r = n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if li[mid] > k:
            r = mid - 1
        elif li[mid] < k:
            l = mid + 1
        else:
            return mid


if __name__ == '__main__':
    li = [1, 3, 7, 34, 45, 65]
    ret = bin_search(li, 34)
    print(ret)
