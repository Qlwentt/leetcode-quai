from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = deque([])
        self.sum = 0

    def next(self, val: int) -> float:
        self.arr.appendleft(val)
        self.sum += val
        if len(self.arr) > self.size:
            outgoing = self.arr.pop()
            self.sum -= outgoing
        return self.sum / len(self.arr)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)