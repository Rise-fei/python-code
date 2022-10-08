"""
给你一个整数数组 nums。你可以选定任意的正数 startValue 作为初始值。
你需要从左到右遍历 nums数组，并将 startValue 依次累加上nums数组中的值。
请你在确保累加和始终大于等于 1 的前提下，选出一个最小的正数作为 startValue 。

贪心
"""


def solution(nums):
    total = 0
    min_val = 0
    for num in nums:
        total += num
        if total <= 0:
            temp = 1 - total
            total = 1
            min_val += temp
    return min_val if min_val > 0 else 1


nums = [-3, 2, -3, 4, 2]
nums = [1, 2]
ret = solution(nums)
print(ret)








