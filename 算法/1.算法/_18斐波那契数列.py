# 斐波那契数列
# 0  1  1  2 3 5 8 13 21

# 双指针解法1  O(N) O(1)
'''
l = [0,1]
pprev = 0
prev = 1
for i in range(20):
    if i > 1:
        cur = prev + pprev
        l.append(cur)
        pprev = prev
        prev = cur
print(l)
print(len(l))
'''
# 双指针解法2  O(N) O(1)
'''
l = [0,1]
pprev = 0
prev = 1
for i in range(0,20,2):
    if i > 1:
        cur = prev + pprev
        prev = cur + prev
        pprev = cur
        l.append(pprev)
        l.append(prev)

print(l)
print(len(l))
print('*********************')
'''
import time
# 暴力递归  O（2**n）
'''
def feibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return feibo(n-1) + feibo(n-2)

l = []
start = time.time()
for i in range(35):
    l.append(feibo(i))
end = time.time()
print(l)
print(end-start)
'''
# 二叉树剪枝递归  O（N） O（N）
'''
l = []
di = {}
def feibo2(n):
    if n == 1:
        di[1] = 1
        return 1
    elif n == 0:
        di[0] = 0
        return 0
    else:
        if di.get(n):
            return di.get(n)
        else:
            di[n] = feibo2(n-1) + feibo2(n-2)
            return di.get(n)

start = time.time()
for i in range(35):
    l.append(feibo2(i))
end = time.time()
print(l)
print(end-start)
'''



