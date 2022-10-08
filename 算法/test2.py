li = [1, 2, 0, 9, 8, 5]


def partition(li, left, right):
    # 对序列进行分区，找一个基准值，将所有比他小的放他左边，比他大的放他右边
    base = li[left]
    while left < right:
        while left < right and li[right] > base:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < base:
            left += 1
        li[right] = li[left]
    li[left] = base
    return left


def quick_sort(li, start, end):
    if start < end:
        mid = partition(li, start, end)
        quick_sort(li, 0, mid - 1)
        quick_sort(li, mid, end)


quick_sort(li, 0, len(li) - 1)
