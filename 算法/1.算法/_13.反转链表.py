# Definition for singly-linked list.
'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归解决（栈）
class Solution:
    def solu(self,node):
        if node is None or node.next is None:
            self.ret_node = node
            return node
        else:
            s = self.solu(node.next)
            s.next = node
            return node

    def reverseList(self, head: ListNode):
        self.ret_node = None
        ret = self.solu(head)
        if ret:
            ret.next = None
        return self.ret_node

# 迭代解决
class Solution2:
    def solu(self,node):
        prev = None
        cur = node

        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev
