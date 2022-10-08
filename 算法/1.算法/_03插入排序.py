# 插入排序 O(N^2)

l = [1,2,7,85,6,45,21,23,45]
length = len(l)

for j in range(1,length):
    i = j
    while i > 0 and l[i] < l[i-1]:
        l[i],l[i-1] = l[i-1],l[i]
        i -= 1
print(l)

