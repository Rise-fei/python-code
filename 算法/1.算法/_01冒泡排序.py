# 冒泡排序   O(N^2)

li = [1, 2, 7, 85, 6, 45, 21, 23, 45]


def bubble_sort(l):
    length = len(l)
    for i in range(length - 1, 0, -1):
        count = 0
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                count += 1
        if count == 0:
            return


bubble_sort(li)
print(li)
