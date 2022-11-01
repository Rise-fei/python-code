# 合并两个有序数组    双指针
l1 = [1,4,5,7,9]
l2 = [2,3,5,8,10]

lg1 = len(l1)
lg2 = len(l2)
i = 0
j = 0
ret = []
while i <= lg1 or j <= lg2:
    if i == lg1:
        while j < lg2:
            ret.append(l2[j])
            j += 1
        break
    if j == lg2:
        while i < lg1:
            ret.append(l1[i])
            i += 1
        break
    v1 = l1[i]
    v2 = l2[j]
    if v1 < v2:
        ret.append(v1)
        i += 1
    else:
        ret.append(v2)
        j += 1
print(ret)