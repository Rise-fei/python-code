import queue


class TreeNode():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的先序 序列化

def travel(root, queue):
    if root is None:
        queue.put("#")
    else:
        queue.put(root.val)
        travel(root.left, queue)
        travel(root.right, queue)


# 二叉树的中序 序列化
def travel2(root, queue):
    if root is None:
        queue.put("#")
    else:
        travel2(root.left, queue)
        queue.put(root.val)
        travel2(root.right, queue)


# 二叉树的后序 序列化

def travel3(root, queue):
    if root is None:
        queue.put("#")
    else:
        travel3(root.left, queue)
        travel3(root.right, queue)
        queue.put(root.val)


if __name__ == "__main__":
    node7 = TreeNode(7, None, None)
    node6 = TreeNode(6, None, None)
    node5 = TreeNode(5, None, None)
    node4 = TreeNode(4, node7, None)
    node3 = TreeNode(3, None, node6)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)

    q = queue.Queue()
    q2 = queue.Queue()
    q3 = queue.Queue()

    travel(node1, q)
    travel2(node1, q2)
    travel3(node1, q3)
    li = []
    li2 = []
    li3 = []
    while not q.empty():
        li.append(q.get())
    while not q2.empty():
        li2.append(q2.get())
    while not q3.empty():
        li3.append(q3.get())
    print(li)
    print(li2)
    print(li3)
