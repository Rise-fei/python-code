class CQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def appendTail(self, value: int) -> None:
        self.q1.append(value)

    def deleteHead(self) -> int:
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())
        return -1 if not self.q2 else self.q2.pop()

