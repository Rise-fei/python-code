"""
输入链表头结点，奇数长度返回中点，偶数长度返回上中点       1 2 3 4      - -2
输入链表头结点，奇数长度返回中点，偶数长度返回下中点
输入链表头结点，奇数长度返回中点前一个，偶数长度返回上中点前一个
输入链表头结点，奇数长度返回中点前一个，偶数长度返回下中点前一个

基于快慢指针，慢指针走1步， 快指针走2步；最终慢指针所在位置就是中点附近位置
"""
from _0base import ListNode, generate_link_list


li = [1, 2, 3, 4, 5, 6, ]
head = generate_link_list(li)
print(head)


def func1(head: ListNode):
    """输入链表头结点，奇数长度返回中点，偶数长度返回上中点"""
    # 12345     3
    # 1234      2
    if not head or not head.next or not head.next.next:
        return head

    slow = head.next
    fast = head.next.next

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def func2(head: ListNode):
    """输入链表头结点，奇数长度返回中点，偶数长度返回下中点"""
    # 12345     3
    # 1234      3
    if not head or not head.next:
        return head
    if not head.next.next:
        return head.next

    slow = head.next
    fast = head.next.next

    while fast.next:
        if fast.next.next:
            slow = slow.next
            fast = fast.next.next
        else:
            return slow.next

    return slow


def func3(head: ListNode):
    """输入链表头结点，奇数长度返回中点前一个，偶数长度返回上中点前一个"""
    # 12345     2
    # 1234      1
    if not head or not head.next or not head.next.next:
        return head

    slow = head
    fast = head.next.next

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def func4(head: ListNode):
    """输入链表头结点，奇数长度返回中点前一个，偶数长度返回下中点前一个"""
    if not head or not head.next or not head.next.next:
        return head

    slow = head
    fast = head.next.next

    while fast.next:
        if fast.next.next:
            slow = slow.next
            fast = fast.next.next
        else:
            return slow.next

    return slow



mid = func1(head)
print(mid.val)
mid = func2(head)
print(mid.val)
mid = func3(head)
print(mid.val)
mid = func4(head)
print(mid.val)

