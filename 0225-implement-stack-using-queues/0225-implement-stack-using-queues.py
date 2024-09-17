from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque([])
        self.last = None

    def push(self, x: int) -> None:
        self.q.append(x) 
        self.last = x

    def pop(self) -> int:
        for _ in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()