"""
求解一个给定的方程，将x以字符串 "x=#value"的形式返回。该方程仅包含 '+' ， '-' 操作，变量x和其对应系数。
如果方程没有解，请返回"No solution"。如果方程有无限解，则返回 “Infinite solutions” 。
题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。

输入: equation = "x+5-3+x=6+x-2"
输出: "x=2"
"""


def solution(s):
    s = s.replace("-", "+-")
    ret = s.split("=")
    left = ret[0]
    right = ret[1]
    l1 = left.split("+")
    l2 = right.split("+")
    num1 = 0
    num2 = 0
    num_x = 0
    num_x2 = 0
    for i in l1:
        if not i:
            continue
        if 'x' not in i:
            num1 += int(i)
        elif i == "x":
            num_x += 1
        elif i == "-x":
            num_x -= 1
        else:
            num_x += int(i[:-1])

    for i in l2:
        if not i:
            continue
        if 'x' not in i:
            num2 += int(i)
        elif i == "x":
            num_x2 += 1
        elif i == "-x":
            num_x2 -= 1
        else:
            num_x2 += int(i[:-1])
    l = (num_x - num_x2)
    r = (num2 - num1)
    if l == 0:
        return "Infinite solutions" if r == 0 else "No solution"
    return "x=%s" % int(r / l)


# ret = solution("x+5-3+x=6+x-2")
# print(ret)
# ret = solution("x=x")
# print(ret)
ret = solution("1-x+x-x+x+x=99")
print(ret)

