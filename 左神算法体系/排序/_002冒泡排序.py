# 冒泡排序

def bubble_sort(li):
    n = len(li)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j+1] = li[j+1], li[j]


def bubble_sort2(li):
    n = len(li)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


if __name__ == '__main__':
    l = [2, 1, 5, 10, 7]
    bubble_sort(l)
    print(l)
    l = [2, 1, 5, 10, 7]
    bubble_sort2(l)
    print(l)