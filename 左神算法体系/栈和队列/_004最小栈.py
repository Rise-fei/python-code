"""
设计栈，每次提取当前栈中的最小值   要求O（1）
两个栈，一个普通栈，一个辅助栈存放当前栈最小值
"""

import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        self.min_val = math.inf

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.min_val:
            self.min_val = x
            self.min_stack.append(x)

    def pop(self) -> None:
        top = self.stack.pop()
        if top <= self.min_val:
            self.min_stack.pop()
            self.min_val = self.min_stack[-1] if self.min_stack else math.inf
        return top

    def top(self) -> int:
        return self.stack[-1]

    def min(self):
        return self.min_val if self.min != math.inf else None
