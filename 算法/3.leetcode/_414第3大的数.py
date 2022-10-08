"""
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
"""


def solution(li):
    li = list(set(li))
    li.sort(reverse=True)
    return li[0] if len(li) < 3 else li[2]


ret = solution([1, 2])
print(ret)
