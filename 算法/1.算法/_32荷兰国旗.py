"""
荷兰国旗问题（快排前置）
给定一个数组，及1个num  将比num小的放左边
比num大的放右边
"""


class Solution:
    def partition(self, li, left, right, base):
        val = li[base]
        li[left], li[base] = li[base], li[left]
        while left < right:
            while left < right and li[right] >= val:
                right -= 1
            li[left] = li[right]

            while left < right and li[left] <= val:
                left += 1
            li[right] = li[left]
        li[left] = val
        return li

    def partition2(self, li):
        """分2个区域，左边为<=基准值的  右边为> 基准值的"""
        val = li[-1]
        left = 0
        for i in range(len(li)):
            if li[i] <= val:
                if i != left:
                    li[i], li[left] = li[left], li[i]
                left += 1
        return li


li = [3, 5, 6, 7, 4, 13, 2, 8, 7, 6]
s = Solution()
# ret = s.partition(li, 0, len(li) - 1, 4)
# print(ret)
# ret2 = s.partition2(li)
# print(ret2)
print("*" * 20)
