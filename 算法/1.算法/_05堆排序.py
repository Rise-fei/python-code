# 堆排序    利用  最大堆的向下调整
# 算法复杂度 nlogn

# 调整函数
def sift(li, low, high):
    '''
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    '''
    i = low
    j = 2 * i + 1  # 左孩子节点
    tmp = li[low]
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果有孩子首先得有右孩子  并且  左孩子比右孩子小
            j = j + 1  # j 指向有孩子
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def heap_sort(li):
    '''
    堆排序
    :param li:
    :return:
    '''
    # 先构造堆,找到完全二叉树的最后一个根节点，从他开始 依次遍历到 根节点 0
    n = len(li)
    # 建堆  ---》 构造为一个最大堆！！
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)

    # 向下调整
    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)

