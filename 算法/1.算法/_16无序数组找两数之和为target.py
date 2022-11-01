# 给定一个无序数组，找出两个数字之和为target的下标

l = [1,5,3,4,6,59,78,12,42]
target = 65

# O（n**2）
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j] == target:
            print(i,j)

# O（N）
di = {}
for index,val in enumerate(l):
    if di.get(target - val):
        print(index,di.get(target - val))
        break
    di[val] = index