

# 快速排序   n*log(n)
# 最坏情况   O(N^2)
# 快排优化：取基准值时，不取第一个 而是随机取区间中一个，然后和第一个位置交换。

li = [1, 2, 7, 85, 6, 45, 21, 23, 45]
length = len(li)


def partition(li, left, right):
    '''
    分区即 找到 某个数的坐标
    :param li:
    :param left:
    :param right:
    :return: 返回基准值的最终坐标
    '''
    # 先找基准值，一般就取第一个即可。----------   快排优化：取基准值时，不取第一个 而是随机取区间中一个，然后和第一个位置交换。
    val = li[left]
    while left < right:
        while left < right and li[right] >= val:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= val:
            left += 1
        li[right] = li[left]
    li[left] = val
    return left


def quick_sort(li, start, end):
    if start < end:
        # 分区
        mid = partition(li, start, end)

        # 左分区排序
        quick_sort(li, start, mid - 1)

        # 右分区排序
        quick_sort(li, mid + 1, end)


quick_sort(li, 0, length - 1)
print(li)


def partition2(li, left, right):
    # 取基准
    val = li[left]
    while left < right:
        while left < right and li[right] >= val:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < val:
            left += 1
        li[right] = li[left]

    # 最后 left==right的时候，即基准所在位置，左边是比他小的  右边是比他大的
    li[left] = val
    return left


def s(li, left, right):
    if left < right:
        mid = partition2(li, left, right)
        s(li, left, mid - 1)
        s(li, mid + 1, right)
