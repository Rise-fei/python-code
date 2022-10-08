"""
最小和
要求： nlogn
给定一个数组，每个数字前面比该数小就累加为该数的最小和
[3,2,5,4,8]
3 -- 0
2 -- 0
5 -- 3 + 2
4 -- 3 + 2
8 -- 3 + 2 + 5 + 4 + 8
total -- 累加  3+2 +3+2 +3+2+5+4+8

思路转换：
3 -- 后边有3个比3大的 即 3*3   3个3为后边数的最小和 计算步骤之一
2 -- 后边有3个比2大的 即 2*3
5 -- 1*5
4 -- 1*4
8 -- 0
total -- 3*3 + 2*3 + 5 + 4 = 9 + 6 + 5 + 4 = 24

利用归并排序，每次merge的时候，将该merge区间的最小和求出，累加
"""
total = 0


def merge(li, low, mid, high):
    global total
    i = low
    j = mid + 1
    ltemp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltemp.append(li[i])
            # 在此处添加 每次merge的时候，将左侧小的值对应 是右侧几个数的最小和 累加起来
            total += li[i] * (high - j + 1)
            i += 1

        else:
            ltemp.append(li[j])
            j += 1
    while i <= mid:
        ltemp.append(li[i])
        i += 1
    while j <= high:
        ltemp.append(li[j])
        j += 1

    li[low:high+1] = ltemp


def merge_sort(li, low, high):
    if low < high:
        # 位右移一位 == 值/2
        mid = low + ((high-low) >> 1)
        # mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


li = [3, 2, 5, 4, 8]
merge_sort(li, 0, len(li) - 1)
print(li)
print(total)
