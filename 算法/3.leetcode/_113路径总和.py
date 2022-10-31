from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum = targetSum
        self.ret = []
        if root is None:
            return []

        self.travel(root, [])
        print(self.ret)
        return self.ret

    def travel(self, root, val_list):

        val_list.append(root.val)

        if not root.left and not root.right:
            if sum(val_list) == self.targetSum:
                print(val_list)
                self.ret.append(val_list.copy())
                print(self.ret)

        if root.left:
            self.travel(root.left, val_list)

        if root.right:
            self.travel(root.right, val_list)

        val_list.pop()


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



s = Solution()
s.pathSum(node1, 22)


