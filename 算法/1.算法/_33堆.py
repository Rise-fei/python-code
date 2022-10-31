"""
堆
heap_insert && heapify

heap_insert: 构建一个大根堆或小根堆
heapify: 基于某个根节点向下调整为一个大根堆或小根堆
[4, 8, 6, 3, 7, 9, 1, 2, 5, 0]
          4
    8         6
  3    7       9   1
2  5  0

"""
# 基于某个节点insert到堆


def heap_insert(li, index):
    # 构建堆
    while index > 0 and li[index] > li[(index - 1) // 2]:
        li[index], li[(index-1)//2] = li[(index-1)//2], li[index]
        index = (index - 1) // 2


def heapify(li, head, tail):
    # 堆的向下调整
    i = head
    j = head * 2 + 1
    while j <= tail:
        # 指向左右孩子节点中最大的孩子节点
        largest = j + 1 if j + 1 <= tail and li[j+1] > li[j] else j
        if li[largest] > li[i]:
            li[largest], li[i] = li[i], li[largest]
            i = largest
            j = 2 * i + 1
        else:
            break


def heapify2(li, head, tail):
    i = head
    j = 2 * i + 1
    while j <= tail:
        if j + 1 <= tail and li[j+1] > li[j]:
            j = j + 1
        if li[j] > li[i]:
            li[i], li[j] = li[j], li[i]
            i = j
            j = 2 * i + 1
        else:
            break


def heap_sort(li):
    n = len(li)

    # 构造堆
    # 方式1： O(nlog n)
    # heap_insert
    # for i in range(n):
    #     heap_insert(li, i)

    # （optimize）方式2： O(n) 等差数列可证！
    # 建堆  ---》 构造为一个最大堆！！
    for i in range((n - 2) // 2, -1, -1):
        heapify2(li, i, n - 1)

    for i in range(len(li)-1, -1, -1):
        li[i], li[0] = li[0], li[i]
        heapify2(li, 0, i-1)


if __name__ == '__main__':

    li = [4, 8, 6, 3, 7, 9, 1, 2, 5, 0]
    heap_sort(li)
    print(li)
