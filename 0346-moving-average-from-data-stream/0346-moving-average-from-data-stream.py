from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque([])
        self.sum = 0
        [1,10,3,5]

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        while len(self.q) > self.size:
            leaving = self.q.popleft()
            self.sum -= leaving
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Time: O(1) for each next to pop and then calculate average, O(N) where n is number of calls to next
# Space: O(k) where k is size of window