"""
链表构建队列

push    head
pop     tail

"""

"""
数组构建队列
见 12-1
"""


from collections import deque
maze = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,1,0,1,0,1],
    [1,0,1,1,0,1,0,1],
    [1,0,0,0,0,1,1,0],
    [1,0,1,1,0,1,1,0],
    [1,0,0,0,0,1,1,1],
    [1,1,1,1,0,1,1,1],
    [1,1,1,1,0,0,0,1],
]

lambs = [
    lambda x,y:(x,y-1),
    lambda x,y:(x+1,y),
    lambda x,y:(x,y+1),
    lambda x,y:(x-1,y),
]

def print_r(path):
    cur = path[-1]
    real_path = []
    while cur[2] != -1:
        real_path.append(cur[0:2])
        cur = path[cur[2]]
    real_path.append(cur[0:2])
    real_path.reverse()
    print(real_path)


def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while len(queue) > 0:
        cur_node = queue.pop()
        path.append(cur_node)

        if cur_node[0] == x2 and cur_node[1] == y2:
            print_r(path)
            return True
        for dir in lambs:
            next_node = dir(cur_node[0],cur_node[1])
            if next_node[0] >= 8 or next_node[1] >= 8:
                continue
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0],next_node[1],len(path)-1))
                maze[next_node[0]][next_node[1]] = 2
    else:
        return False

maze_path_queue(1,1,7,6)


