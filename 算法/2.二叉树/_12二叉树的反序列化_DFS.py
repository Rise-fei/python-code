# 广度优先遍历   使用队列， 遍历的同时 统计最大宽度
import queue


class TreeNode():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的先序 反序列化
def reverseSer(q):
    val = q.get()
    if val == "#":
        return None

    node = TreeNode(val, None, None)
    node.left = reverseSer(q)
    node.right = reverseSer(q)
    return node


# 二叉树的中序 反序列化
def reverseSer2(q):
    pass


# 二叉树的后序 反序列化
def reverseSer3(q):
    pass


li = [1, 2, 4, 7, '#', '#', '#', 5, '#', '#', 3, '#', 6, '#', '#']
li2 = ['#', 7, '#', 4, '#', 2, '#', 5, '#', 1, '#', 3, '#', 6, '#']
li3 = ['#', '#', 7, '#', 4, '#', '#', 5, 2, '#', '#', '#', 6, 3, 1]
q = queue.Queue()
q2 = queue.Queue()
q3 = queue.Queue()

for i in li:
    q.put(i)

for i in li2:
    q2.put(i)

for i in li3:
    q3.put(i)

head = reverseSer(q)
head2 = reverseSer2(q2)
head3 = reverseSer(q3)


from _10二叉树的序列化_DFS import travel, travel2, travel3


q = queue.Queue()
travel(head, q)
li = []
while not q.empty():
    li.append(q.get())
print(li)
