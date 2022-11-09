# 广度优先遍历
import queue


class TreeNode():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def generate_node(d):
    if d:
        return TreeNode(d, None, None)
    else:
        return None


# 二叉树的层序 反序列化【广度优先遍历】
def reverseSer(li, q):
    head_node = generate_node(li.pop())
    if head_node:
        q.put(head_node)

    while not q.empty():
        root = q.get()
        root.left = generate_node(li.pop())
        root.right = generate_node(li.pop())
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)
    return head_node


from _11二叉树的序列化_BFS import serializer

if __name__ == '__main__':

    li = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, None]
    li = li[::-1]
    q = queue.Queue()
    head = reverseSer(li, q)

    q2 = queue.Queue()
    ret = serializer(head, q2)
    print(ret)





