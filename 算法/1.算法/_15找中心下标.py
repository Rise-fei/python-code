li = [6,1,2,2,15,4,5,2,0]


def solution(li):
    length = len(li)

    cur = 0
    total = sum(li)
    for i in range(length-1):
        cur += li[i]
        if cur*2 + li[i+1] == total:
            return i+1




ret = solution(li)
print(ret)



