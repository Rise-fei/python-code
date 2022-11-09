class Linklist:
    def __init__(self, val, node):
        self.val = val
        self.next = node


node5 = Linklist(5, None)
node4 = Linklist(4, node5)
node3 = Linklist(3, node4)
node2 = Linklist(2, node3)
node1 = Linklist(1, node2)

node33 = Linklist(33, node3)
node22 = Linklist(22, node33)
node11 = Linklist(11, node22)

"""
给定两个无环单链表，判断是否相交并返回第一个相交的节点；
解法1： 哈希判断  时间o(n) 空间o(n)
解法2： 遍历     时间o(n) 空间o(1)
"""


def solu(head1, head2):
    """解法1"""
    s = set()

    cur = head1
    while cur:
        s.add(cur)
        cur = cur.next

    cur = head2
    while cur:
        if cur in s:
            return True, cur
        cur = cur.next
    return False, None


def solu2(head1, head2):
    """解法2， 优化空间复杂度"""
    n1 = 0

    cur1 = head1
    while cur1:
        n1 += 1
        cur1 = cur1.next

    n2 = 0
    cur2 = head2
    while cur2:
        n2 += 1
        cur2 = cur2.next

    if cur1 != cur2:
        return False, None

    if n1 > n2:
        diff = n1 - n2
        cur1 = head1
        cur2 = head2
    else:
        diff = n2 - n1
        cur1 = head2
        cur2 = head1

    for i in range(diff):
        cur1 = cur1.next

    while cur2 != cur1:
        cur1 = cur1.next
        cur2 = cur2.next

    return True, cur1


a, b = solu(node1, node11)
print(a, b.val)
a, b = solu2(node1, node11)
print(a, b.val)


def get_loop(head):
    """
    给定一个链表头结点，判断是否成环，如环，返回入环节点
    """
    if head is None or head.next is None:
        return False, None
    slow = head.next
    quick = head.next.next
    while slow != quick:
        if quick is None or quick.next is None:
            return False
        slow = slow.next
        quick = quick.next.next
    quick = head
    while slow != quick:
        slow = slow.next
        quick = quick.next

    return True, quick


"""
给定两个成环链表，判断是否相交，并返回相交节点
"""


def solu3(head1, loop1, head2, loop2):
    if loop1 == loop2:
        n1 = 0
        cur1 = head1
        while cur1 != loop1:
            n1 += 1
            cur1 = cur1.next

        n2 = 0
        cur2 = head2
        while cur2 != loop2:
            n2 += 1
            cur2 = cur2.next

        if n1 > n2:
            diff = n1 - n2
            cur1 = head1
            cur2 = head2
        else:
            diff = n2 - n1
            cur1 = head2
            cur2 = head1

        for i in range(diff):
            cur1 = cur1.next

        while cur2 != cur1:
            cur1 = cur1.next
            cur2 = cur2.next
        return True, cur1

    cur = loop1.next
    while cur != loop1:
        if cur == loop2:
            return True, loop2
        cur = cur.next
    return False, None


e = Linklist(5, None)
d = Linklist(4, e)
c = Linklist(3, d)
b = Linklist(2, c)
a = Linklist(1, b)
e.next = c


h = Linklist(33, b)
g = Linklist(22, h)
f = Linklist(11, g)

h2 = Linklist(33, b)
g2 = Linklist(22, h2)
f2 = Linklist(11, g2)

print("*" * 100)
ok, node1 = get_loop(a)
print(ok, node1.val)
ok, node2 = get_loop(f)
print(ok, node2.val)
# ok, node22 = get_loop(f2)
# print(ok, node22.val)

ok, node3 = solu3(a, node1, f, node2)
print(ok, node3.val)
# ok, node4 = solu3(a, node1, f2, node22)
# print(ok, node4.val)
