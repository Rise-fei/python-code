# 深度优先
class TreeNode():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
# node7 = TreeNode(7,None,None)
# node6 = TreeNode(6,None,None)
# node5 = TreeNode(5,None,None)
# node4 = TreeNode(4,node7,None)
# node3 = TreeNode(3,None,node6)
# node2 = TreeNode(2,node4,node5)
# node1 = TreeNode(1,node2,node3)

node11 = TreeNode(1,None,None)
node10 = TreeNode(5,None,None)
node9 = TreeNode(2,None,None)

node7 = TreeNode(7,None,None)

node8 = TreeNode(4,node10,node11)
node5 = TreeNode(13,None,None)
node4 = TreeNode(11,node7,node9)
node3 = TreeNode(8,node5,node8)
node2 = TreeNode(4,node4,None)
node1 = TreeNode(5,node2,node3)


# 深度遍历  递归遍历
def travel(root):
    if root is None:
        return None
    print(root.val)
    if root.left:
        travel(root.left)

    if root.right:
        travel(root.right)


travel(node1)
