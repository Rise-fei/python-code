# 深度优先  递归遍历
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


def soluMin(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    min_val = 2**32
    if root.left:
        min_val = min(soluMin(root.left),min_val)
    if root.right:
        min_val = min(soluMin(root.right),min_val)

    return min_val + 1

ret = soluMin(node1)
print(ret)

