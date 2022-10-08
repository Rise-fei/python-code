"""
给定一个数组，其中只有1种数字出现了 奇数次， 找出来
 1 1 2 2 2 3  3 3 3 4 4   ---》 2
"""
li = [1, 1, 2, 2, 2, 3, 3]
ret = 0
for i in li:
    ret ^= i
print(ret)
"""
给定一个数组，其中只有2种数字出现了 奇数次， 找出来
1 1 2 2 2 3 3 3 4 4 5 5  ---》 2 3
要求：时间o(n)  空间o(1)
"""
li = [1, 1, 89, 89, 89, 127, 127, 127, 4, 4]
ret = 0
for i in li:
    ret ^= i
# ret 为 a 和 b的异或； a, b为结果; a != b; ret != 0 ----> ret在某一位上肯定有1位是1；即该位上，a和b 不一
# a   1011001  89
# b   1111111  127

# ret 0100110   38
print(ret)
# 找出ret中最后一位1的位置
right_one = ret & (~ret + 1)
# ret               0100110
# ~ret              1011001
# ~ret+1            1011010
# ret & (~ret + 1)  0000010
print(right_one)

only_one = 0
for i in li:
    # 0000010
    # 1111101
    # 0000000
    # li中所有第2位上为0的值都 累异或  （类似累积）
    print("*"*20)
    print(i & right_one)
    print("*"*20)
    if i & right_one == 0:
        only_one ^= i
print(only_one, ret ^ only_one)

