"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。

每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

"""


def isvalid(record, i, j):
    for k in range(i):
        if j == record[k] or abs(i - k) == abs(j - record[k]):
            return False
    return True


def solu(n, record, i, ret):
    # 如果i已经走出棋盘 说明已经产生1种结果了
    if i == n:
        ret.append(translate(record, n))
        return 1

    count = 0
    for j in range(n):
        if isvalid(record, i, j):
            record[i] = j
            count += solu(n, record, i + 1, ret)
    return count


def translate(record_list, n):
    ss = []
    for j in record_list:
        s = ""
        for k in range(n):
            if k == j:
                s += "Q"
            else:
                s += "."
        ss.append(s)
    return ss


if __name__ == '__main__':
    n = 4
    # s = [["." for j in range(n)] for i in range(n)]
    record = [-1 for i in range(n)]
    ret = []
    res = solu(n, record, 0, ret)
    print(ret)
    print(res)
