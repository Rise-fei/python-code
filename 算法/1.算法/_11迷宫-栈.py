maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1],
]

lambs = [
    lambda x, y: (x, y - 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x - 1, y),
]


def maze_path(x1, y1, x2, y2):
    ret = []
    ret.append((x1, y1))
    while (ret):
        cur = ret[-1]
        if cur[0] == x2 and cur[1] == y2:
            for i in ret:
                print(i)
            return True
        for fun in lambs:
            posx, posy = fun(cur[0], cur[1])
            if posx >= 8 or posy >= 8:
                continue
            if maze[posx][posy] == 0:
                ret.append((posx, posy))
                maze[posx][posy] = 2
                break
        else:
            maze[posx][posy] = 2
            ret.pop()
    else:
        return False


maze_path(1, 1, 7, 6)
