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


def merge_sort(li,low,high):
    if low < high:
        mid = (low + high) // 2
        # 归并排序 左边
        merge_sort(li, low, mid)
        # 归并排序 右边
        merge_sort(li, mid + 1, high)
        # 合并排序
        merge(li, low, mid, high)

li = [2,4,6,8,1,3,5,7]
# merge(li,0,3,7)

merge_sort(li,0,7)
print(li)

