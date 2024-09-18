from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque([])
        self.sum = 0
        

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        while len(self.q) > self.size:
            leaving = self.q.popleft()
            self.sum -= leaving
        return self.sum / len(self.q)


# Time: O(N) where n is number of calls to next
# Space: O(k) where k is size of window