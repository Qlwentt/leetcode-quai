from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.q = deque([])
        self.size = size
        self.runSum = 0
        

    def next(self, val: int) -> float:
        self.runSum += val
        self.q.append(val)
        
        if len(self.q) > self.size:
            item = self.q.popleft()
            self.runSum -= item
            
        return self.runSum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)