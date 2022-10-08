# 深度优先
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

# 深度遍历  递归遍历
def travel(root):
    if root is None:
        return None

    if root.left:
        travel(root.left)

    if root.right:
        travel(root.right)
    print(root.val)
travel(node1)
