# 选择排序 O(N^2)
l = [1, 2, 7, 85, 6, 45, 21, 23, 45]
length = len(l)

for i in range(length - 1):
    minindex = i
    for j in range(i + 1, length):
        if l[minindex] > l[j]:
            minindex = j
    if minindex != i:
        l[i], l[minindex] = l[minindex], l[i]
print(l)


def select_sort(l):
    n = len(l)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, length):
            if l[minIndex] > l[j]:
                minIndex = j
        l[i], l[minIndex] = l[minIndex], l[i]


l = [1, 2, 7, 85, 6, 45, 21, 23, 45]
select_sort(l)
print(l)
