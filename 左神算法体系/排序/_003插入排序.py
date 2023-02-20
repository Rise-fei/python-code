# 冒泡排序

def insert_sort(li):
    n = len(li)
    for j in range(1, n):
        i = j
        while i > 0 and li[i] < li[i-1]:
            li[i], li[i-1] = li[i-1], li[i]
            i -= 1


if __name__ == '__main__':
    l = [2, 1, 5, 10, 7]
    insert_sort(l)
    print(l)
