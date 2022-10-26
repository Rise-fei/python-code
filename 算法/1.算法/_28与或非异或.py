"""
基于与运算计算整数的二级制

"""
a = 12321312
for i in range(31,0,-1):
    print(a & (i << i), end="")
print()


"""求一个二进制数中1的个数"""
ss = 1234
print(bin(ss))

count = 0
while ss:
    ss2 = ss & (~ss + 1)
    ss = ss ^ ss2
    count += 1
print("二进制的个数是：", count)


"""
按位 与运算
&
两个位都为1时，结果才为1
【可判断奇数】
"""
ou_li = []
ji_li = []
for i in range(20):
    if i & 1 == 1:
        ou_li.append(i)
    else:
        ji_li.append(i)
print(ou_li)
print(ji_li)
"""
按位 或运算
|
两个位都为0时，结果才为0 
只要有1位为1，结果就为1
"""


"""
异或
^
异或有交换律和结合律；
两个位相同为0，相异为1；
a ^ a = 0

【两数交换】
"""
a = 1
b = 2
# 01
# 10
a = a ^ b
# 11
print(a)
b = a ^ b
print(b)
a = a ^ b
print(a, b)
"""
【异或判断奇偶性】
异或：无进位相加
所有偶数异或 1的结果为 该偶数+1；
1000110 ^ 000001  ==== 1000110 + 1  ==== 1000111
所有奇数异或1的结果为  该奇数-1
11111 ^ 00001 ==== 11111 -1 ==== 11110
"""
for i in range(100, 150):
    if i ^ 1 == i + 1:
        print(i, end=" ")
print()
"""消除最后一位1"""
# 1110
# 1101

# 1100
x = 3
s = x & (x - 1)
print(s)
