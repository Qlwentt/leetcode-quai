from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.nums = deque([])
        self.size = size

    def next(self, val: int) -> float:
        self.nums.append(val)
        while len(self.nums) > self.size:
            self.nums.popleft()
        return (sum(self.nums)) / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)