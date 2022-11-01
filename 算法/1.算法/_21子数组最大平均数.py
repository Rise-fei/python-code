# 滑动窗口
import time
li = [1,12,-5,-6,50,3] * 100000
k = 4
print(li[0:2])
def solu(li,k):
    max_val = 0
    lg = len(li)

    start = 0
    head = 0
    # nex = 0
    s = 0
    while 1:
        end = start + k
        if end > lg:
            return max_val
        else:
            nex = li[end-1]
        # s = sum(li[start:end])       # 此处可优化，每次都需要sum整个区间    ---->  删除首部值  加上下一个值
        if start == 0:
            s = sum(li[0:k])
        else:
            s = s - head + nex

        head = li[start]
        avg = s / k
        if avg > max_val:
            max_val = avg
        start += 1


st = time.time()
ret = solu(li,k)
en = time.time()
print(ret)
print(en-st)
