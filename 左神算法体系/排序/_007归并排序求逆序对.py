"""
逆序对

左边数比右边数大
[3, 2, 5, 4, 0]
3 2
3 0
2 0
5 0
5 4
4 0

"""
total = 0


def merge(li, low, mid, high):
    global total
    i = low
    j = mid + 1
    ltemp = []
    while i <= mid and j <= high:
        if li[i] > li[j]:
            ltemp.append(li[i])
            # 在此处添加 每次merge的时候，将左侧小的值对应 是右侧几个数的最小和 累加起来
            total += (high - j + 1)
            for x in range(j, high+1):
                print(li[i], li[x])

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


li = [3, 2, 5, 4, 0]
merge_sort(li, 0, len(li) - 1)
print(li)
print(total)
