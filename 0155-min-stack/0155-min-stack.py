class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prev_min = self.stack[-1][1] if self.stack else float("inf")
        current_min = min(prev_min, val)
        self.stack.append((val, current_min))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else -1

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()