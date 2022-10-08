# 算法复杂度 nlogk

# 调整函数，得到最小堆
def sift(li,low,high):
    '''
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    '''
    i = low
    j = 2 * i + 1 # 左孩子节点
    tmp = li[low]
    while j <= high: # 只要j位置有数
        if j + 1 <= high and li[j+1] < li[j]: #如果有孩子首先得有右孩子  并且  左孩子比右孩子小
            j = j + 1  # j 指向有孩子
        if tmp > li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp



def topk(li,k):
    heap = li[0:k]
    # 建堆  最小堆
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)

    # 遍历后续值，每一个都判断是否入堆并调整
    for i in range(k,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)

    # 出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap
li = [1,5,7,41,6,54523,45,6,2,32]
ret = topk(li,4)
print(ret)

