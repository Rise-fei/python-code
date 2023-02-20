# 选择排序

def select_sort(li):
    n = len(li)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]



if __name__ == '__main__':
    l = [2, 1, 5, 10, 7]
    select_sort(l)
    print(l)
