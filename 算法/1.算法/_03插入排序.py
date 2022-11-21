# 插入排序 O(N^2)

l = [1, 2, 7, 85, 6, 45, 21, 23, 45]
length = len(l)

for j in range(1, length):
    i = j
    while i > 0 and l[i] < l[i - 1]:
        l[i], l[i - 1] = l[i - 1], l[i]
        i -= 1
print(l)


def insert_sort(li):
    n = len(l)
    for i in range(1, n):
        j = i
        while j > 0 and li[j] < li[j-1]:
            li[j], li[j-1] = li[j-1], li[j]
            j -= 1

l = [1, 2, 7, 85, 6, 45, 21, 23, 45]
insert_sort(l)
print(l)