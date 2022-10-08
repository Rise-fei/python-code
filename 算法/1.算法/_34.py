class ListNode:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = nex

    def __str__(self):
        return f"node({self.val})"


def reverse_linked_list(head_node):
    # 反转链表
    prev = None
    cur = head_node

    while cur:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex
    return prev


def traverse_linked_list(head_node):
    # 遍历链表
    while head_node:
        print(head_node, end=" ")
        head_node = head_node.next
    print()


def create_linked_list_by_array(array_list):
    zero = ListNode(0)
    prev = zero
    for i in array_list:
        cur = ListNode(i)
        prev.next = cur
        prev = cur
    return zero.next


def create_linked_list(length, start=0):
    # 创建链表
    i = length
    nex = None
    while i > start:
        cur = ListNode(i)
        cur.next = nex
        nex = cur
        i -= 1
    return nex


def del_n_th_to_last_node(head_node, n):
    # 删除倒数第n个节点【双指针遍历】
    i = 0
    zero = ListNode(0, head_node)
    cur = head_node
    while cur and i < n:
        i += 1
        cur = cur.next

    if not cur:
        return head_node.next

    while cur:
        cur = cur.next
        zero = zero.next
    zero.next = zero.next.next
    return head_node


def merge_sorted_linked_list(node1, node2):
    # 合并两个有序链表
    h = ListNode(0)
    cur = h
    while node1 and node2:
        v1 = node1.val
        v2 = node2.val
        if v1 <= v2:
            cur.next = node1
            node1 = node1.next
        else:
            cur.next = node2
            node2 = node2.next
        cur = cur.next
    if not node1:
        cur.next = node2
    else:
        cur.next = node1
    # while node1:
    #     cur.next = node1
    #     cur = cur.next
    #     node1 = node1.next
    # while node2:
    #     cur.next = node2
    #     cur = cur.next
    #     node2 = node2.next
    return h.next


if __name__ == '__main__':
    head = create_linked_list(10)
    traverse_linked_list(head)
    reverse_head = reverse_linked_list(head)
    traverse_linked_list(reverse_head)

    head = create_linked_list(10)
    del_head = del_n_th_to_last_node(head, 2)
    traverse_linked_list(del_head)

    # h1 = create_linked_list(5)
    # h2 = create_linked_list(10, 5)
    h1 = create_linked_list_by_array([1, 3, 5, 8, 9])
    h2 = create_linked_list_by_array([2, 4, 5, 6, 7])

    m = merge_sorted_linked_list(h1, h2)
    print(m)
    traverse_linked_list(m)

    h = create_linked_list_by_array([3, 4, 5, 3, 1])
    traverse_linked_list(h)
