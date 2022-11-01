# 给定一个有序数组，找出两个数字之和为target的下标
# 解法1   暴力双循环  O(N**2)    O（1）
# 解法2   map存储    O(N)  但是需要创建字典，空间复杂度O（N）
# 解法3   遍历+二分   O(n*logN)  O(1)
l = [1,3,4,6,59,78,100]
target = 79
def solu(l,target):
    for i in range(len(l)):
        # cur_val = l[i]
        left = i
        right = len(l) - 1
        while left <= right:
            mid = (left + right) // 2
            if l[i] + l[mid] == target:
                return i,mid
            elif l[i] + l[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
ret = solu(l,target)
print(ret)

# 解法4   双指针    O(N) O(1)

def doublepoint(l,target):
    left = 0
    right = len(l) - 1
    while left < right:
        if l[left] + l[right] == target:
            return left, right
        elif l[left] + l[right] > target:
            right -= 1
        else:
            left += 1
ret = doublepoint(l,target)
print(ret)
