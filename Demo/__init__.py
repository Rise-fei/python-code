class ListNode:
    def __init__(self, key, val, nex=None, pre=None):
        self.key = key
        self.val = val
        self.next = nex
        self.prev = pre


class LRUCache:

    def print_list(self):
        s = ""
        cur = self.head

        while cur:
            s += "key({})val({}) --> ".format(cur.key, cur.val)
            cur = cur.next
        print(s)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.mapping = {
            # 'first': Node1
        }

    def update_node_to_head(self, node):
        if node == self.head:
            return
        if node == self.tail:
            prev = self.tail.prev
            if prev:
                prev.next = None
                self.tail = prev
            else:
                return

        elif node != self.head:
            # 非头结点时，将该节点放到头结点
            node.prev.next = node.next
            node.next.prev = node.prev

        # 将节点移入头部
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        # 查询节点
        if node := self.mapping.get(key):
            # 如果查询到节点,将该节点移到头结点
            self.update_node_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:

        if self.mapping.get(key):
            # 更新原来的key， 将该节点移到头结点
            node = self.mapping[key]
            node.val = value
            self.update_node_to_head(node)

        else:
            node = ListNode(key, value)
            # 判断长度，如果已经到达capacity，则删除为节点，从头节点插入
            if self.size >= self.capacity:
                # 将该节点替换为尾节点
                prev = self.tail.prev
                del self.mapping[self.tail.key]

                if prev:
                    prev.next = node
                    node.prev = prev
                    self.tail = node
                    self.update_node_to_head(node)
                else:
                    self.head = node
                    self.tail = node


            else:
                # 新增节点至头结点

                if self.head:
                    self.head.prev = node
                    node.next = self.head
                    node.prev = None
                    self.head = node

                else:
                    self.head = node
                    self.tail = node

                self.size += 1
            self.mapping[key] = node



#  4  3  2
# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(10)
# lRUCache.put(1,1)
# lRUCache.get(1)
s1 = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
s2 = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

for i, d in enumerate(s1):
    if s2[i] == [2]:
        pass
    if d == "put":
        k = s2[i][0]
        v = s2[i][1]
        lRUCache.put(k, v)
        print("Put {}:{}".format(k,v))
    else:
        k = s2[i][0]
        s = lRUCache.get(k)
        print(f"GET {k}: ret:{s}")
    lRUCache.print_list()

