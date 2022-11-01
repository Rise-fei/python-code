from _0base import ListNode, generate_link_list

li = [1, 2, 3, 3, 2, 1]
head = generate_link_list(li)
print(head)
"""
遍历1遍链表 ， 入栈
再次遍历链表  出栈对比
"""


def func(head):
    stack = []
    cur = head
    while cur:
        stack.append(cur.val)
        cur = cur.next

    cur = head
    while cur:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    return True


"""
优化， 基于快慢指针；
慢指针在奇数中点或偶数的上中点
慢指针之后的节点值入栈；从头结点依次遍历和 栈中的值比对，直到栈空
"""
def midOrUp(head: ListNode):
    """输入链表头结点，奇数长度返回中点，偶数长度返回上中点"""
    if not head or not head.next or not head.next.next:
        return head

    slow = head.next
    fast = head.next.next

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def func2(head):
    mid = midOrUp(head)
    stack = []
    cur = mid.next
    while cur:
        stack.append(cur.val)
        cur = cur.next

    cur = head
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    return True


# print(head)
# head = head.reverse_linked_list()
# print(head)


"""
链表逆序             
空间O(1)

先快慢指针走到中点
将慢指针后的节点逆序
然后从两边开始遍历到中点并比对

"""


def optimize_func(head):
    left_head = head
    mid = midOrUp(head)

    right = mid.next
    mid.next = None

    right_head = right.reverse_linked_list()

    right_cur = right_head
    left_cur = left_head
    while right_cur:
        if right_cur.val != left_cur.val:
            return False
        right_cur = right_cur.next
        left_cur = left_cur.next
    return True


ret = func(head)
print(ret)

ret = func2(head)
print(ret)

ret = optimize_func(head)
print(ret)
