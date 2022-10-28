# 归并排序,python内置排序使用
# 算法复杂度 nlogn

def merge(li,low,mid,high):
    i = low
    j = mid + 1
    ltemp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltemp.append(li[i])
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


def merge_sort(li):
    # 非递归实现
    length = len(li)
    if length < 2:
        return
    """
    分左右两组，然后合并两组
    
    """
    max_size = 1
    while max_size < length:
        l = 0
        while l < length:
            l2 = l + max_size - 1
            if l2 > length:
                break
            r = l2 + 1
            r2 = (r + max_size - 1) if (r + max_size - 1) < (length - 1) else (length - 1)
            merge(li, l, l2, r2)
            l = r2 + 1

        max_size <<= 1


li = [2,4,6,8,1,3,5,7,12,32,1,-1]

merge_sort(li)
print(li)

