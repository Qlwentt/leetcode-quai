from sortedcontainers import SortedSet
class MedianFinder:

    def __init__(self):
        self.i = 0
        self.list = SortedSet()
        

    def addNum(self, num: int) -> None:
        self.list.add((num, self.i))
        self.i+= 1
        

    def findMedian(self) -> float:
        n = len(self.list)
        if n % 2:
            return self.list[n//2][0]
        else:
            return (self.list[n//2-1][0] + self.list[n//2][0]) /2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()