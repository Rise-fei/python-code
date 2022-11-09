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

# 深度遍历  迭代遍历（栈）

def travel(root):
    """头右左   ---  左右头（后序遍历的逆序）"""
    if root is None:
        return
    stack = []
    stack2 = []
    stack.append(root)

    while stack:
        root = stack.pop()
        stack2.append(root)
        if root.left:
            stack.append(root.left)

        if root.right:
            stack.append(root.right)

    while stack2:
        print(stack2.pop().val)

def travel2(root):
    if root is None:
        return
    stack = []
    prev = TreeNode(None,None,None)
    while stack or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.right is None or root.right == prev:
            print(root.val)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right

travel(node1)
travel2(node1)