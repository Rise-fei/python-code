"""
定义链表的基础结构

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ret = ""
        node = self
        while node:
            ret += str(node.val) + " "
            node = node.next
        return ret

    def reverse_linked_list(self):
        prev = None
        cur = self

        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev


def generate_link_list(li):
    head = None
    pre = None
    for i in li:
        cur = ListNode(i)
        if pre:
            pre.next = cur
        else:
            head = cur
        pre = cur
    pre.next = None
    return head


