# 深度优先
class TreeNode():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


node7 = TreeNode(7, None, None)
node6 = TreeNode(6, None, None)
node5 = TreeNode(5, None, None)
node4 = TreeNode(4, node7, None)
node3 = TreeNode(3, None, node6)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)


# 深度遍历  递归遍历
def travel(root, i, li):
    if root is None:
        return None
    li.append((i, root.val))

    if root.left:
        travel(root.left, 2 * i, li)

    if root.right:
        travel(root.right, 2 * i + 1, li)


# 递归过程中，借助列表存储 每个节点的索引和val   递归结束后，遍历列表！
li = []
travel(node1, 1, li)
print(li)
ret = sorted(li, key=lambda x: x[0])
print(ret)
for i in ret:
    print(i[1])
