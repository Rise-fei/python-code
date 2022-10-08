class Linklist():
    def __init__(self,val,node):
        self.val = val
        self.next = node

node5 = Linklist(5,None)
node4 = Linklist(4,node5)
node3 = Linklist(3,node4)
node2 = Linklist(2,node3)
node1 = Linklist(1,node2)
node5.next = node3

# 解法1，遍历  容器存对象判断  O（N）  O(N)
def solu(node1):
    li = []
    node = node1
    while node.next:
        if node in li:
            return True
        else:
            li.append(node)
            node = node.next
    return False
ret = solu(node1)
print(ret)

# 解法2 双指针（慢指针[走一步] + 快指针[走两步]，如果有环，快慢指针早晚会重叠）   O（N）  O(1)

def solu2(head):
    if head is None or head.next is None:
        return False
    slow = head
    quick = head.next
    while slow != quick:
        if quick is None or quick.next is None:
            return False
        slow = slow.next
        quick = quick.next.next
    return True


ret = solu2(node1)
print(ret)