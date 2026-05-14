class MinStack:

    def __init__(self):
        self.main = []
        self.mini = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if (len(self.mini) > 0 and val <= self.mini[-1]) or (len(self.mini) == 0):
            self.mini.append(val)

    def pop(self) -> None:
        if self.main[-1] == self.mini[-1]:
            self.mini.pop()
        return self.main.pop()

    def top(self) -> int:
        return self.main[-1]
        

    def getMin(self) -> int:
        if len(self.mini) > 0:
            return self.mini[-1]
