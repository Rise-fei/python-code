# 广度优先  队列

import queue
class TreeNode():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
        self.deep = None
node7 = TreeNode(7,None,None)
node6 = TreeNode(6,None,None)
node5 = TreeNode(5,None,None)
node4 = TreeNode(4,node7,None)
node3 = TreeNode(3,None,node6)
node2 = TreeNode(2,node4,node5)
node1 = TreeNode(1,node2,node3)


def soluMin(root):
    if root is None:
        return 0

    q = queue.Queue()
    q.put(root)
    root.deep = 1

    while not q.empty():
        node = q.get()
        if node.left is None and node.right is None:
            return node.deep
        if node.left:
            q.put(node.left)
            node.left.deep = node.deep + 1
        if node.right:
            q.put(node.right)
            node.right.deep = node.deep + 1

ret = soluMin(node1)
print(ret)