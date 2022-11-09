import queue


class TreeNode():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的层序 序列化
def serializer(root, queue):
    ret = []
    if not root:
        ret.append(None)
    else:
        ret.append(root.val)
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if node.left:
                ret.append(node.left.val)
                queue.put(node.left)
            else:
                ret.append(None)

            if node.right:
                ret.append(node.right.val)
                queue.put(node.right)
            else:
                ret.append(None)
    return ret


if __name__ == "__main__":
    node7 = TreeNode(7, None, None)
    node6 = TreeNode(6, None, None)
    node5 = TreeNode(5, None, None)
    node4 = TreeNode(4, node7, None)
    node3 = TreeNode(3, None, node6)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)

    q = queue.Queue()

    ret = serializer(node1, q)
    print(ret)
