"""
数组构建队列

循环数组，给定长度的数组，构建队列

"""


class MyQueue:

    def __init__(self, limit):
        self.size = 0
        self.limit = limit
        self.index = 0
        self.li = [0 for _ in range(limit)]
        self.pop_index = 0
        self.push_index = 0

    def get_next_index(self, index):
        # 如果长度溢出，归零
        return index + 1 if index < self.limit - 1 else 0

    def push_value(self, value):
        if self.size == self.limit:
            raise Exception("超出长度限制")
        self.size += 1
        self.li[self.push_index] = value
        self.push_index = self.get_next_index(self.push_index)

    def pop_value(self):
        if self.size == 0:
            raise Exception("空队列，无法得到新数据")
        self.size -= 1
        val = self.li[self.pop_index]
        self.pop_index = self.get_next_index(self.pop_index)
        return val


my_queue = MyQueue(5)
print(my_queue.li)
my_queue.push_value(1)
print(my_queue.li)
my_queue.push_value(2)
print(my_queue.li)
my_queue.push_value(3)
print(my_queue.li)
my_queue.push_value(4)
print(my_queue.li)
my_queue.push_value(5)
print(my_queue.li)
print(my_queue.pop_value())
print(my_queue.pop_value())
print(my_queue.pop_value())
print(my_queue.pop_value())
print(my_queue.pop_value())

