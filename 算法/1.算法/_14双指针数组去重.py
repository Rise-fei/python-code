li = [0,1,2,2,3,3,4,5]


def solution(li):
    if len(li) <= 1:
        return len(li)
    else:
        i = 0
        for j in range(1,len(li)):
            if li[j] != li[i]:
                i += 1
                li[i] = li[j]
        return i + 1
ret = solution(li)
print(li)
print(ret)
