class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        currentMin = self.stack[-1][1] if self.stack else float('inf')
        thisMin = min(currentMin, val)
        self.stack.append((val, thisMin))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# O(1) time for all operations
# O(2n) space = O(n)