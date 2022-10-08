# 广度优先遍历   使用队列
import queue

class TreeNode():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
node7 = TreeNode(7,None,None)
node6 = TreeNode(6,None,None)
node5 = TreeNode(5,None,None)
node4 = TreeNode(4,node7,None)
node3 = TreeNode(3,None,node6)
node2 = TreeNode(2,node4,node5)
node1 = TreeNode(1,node2,node3)


def travel(root):
    q = queue.Queue()
    if root is None:
        return None

    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.val)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
travel(node1)

