class MinStack:

    def __init__(self):
        self.s1 = []
        self.smin = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.smin or val <= self.smin[-1]:
            self.smin.append(val)


    def pop(self) -> None:
        if self.s1[-1] == self.smin[-1]:
            self.smin.pop()
        self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.smin[-1]
