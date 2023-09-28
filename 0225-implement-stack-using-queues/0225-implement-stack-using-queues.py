from collections import deque

class MyStack:

    def __init__(self):
        self.front = deque([])
        self.end = deque([])

    def push(self, x: int) -> None:
        while self.end:
            self.front.append(self.end.popleft())
        self.front, self.end = self.end, self.front
        self.front.append(x)
        
        

    def pop(self) -> int:
        item = self.front.popleft()
        if self.end:
            self.front.append(self.end.popleft())
        return item

    def top(self) -> int:
        return self.front[0]

    def empty(self) -> bool:
        return len(self.front) == 0 and len(self.end) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()