class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self,val):
        heapq.heappush(self.heap, val * -1)
        
    def top(self):
        return self.heap[0] * -1
        
    def pop(self):
        return heapq.heappop(self.heap) * -1
    
    def length(self):
        return len(self.heap)
class MedianFinder:

    def __init__(self):
        self.small = MaxHeap()
        self.large = []

    def addNum(self, num: int) -> None:
        self.small.push(num)
        
        # max value in small is greater than min value in large
        if self.small.length() > 0 and self.large and self.small.top() > self.large[0]:
            tooBig = self.small.pop()
            heapq.heappush(self.large, tooBig)
        
        if abs(self.small.length() - len(self.large)) > 1:
               #small is too big
            if self.small.length() > len(self.large):
                tooBig = self.small.pop()
                heapq.heappush(self.large, tooBig)
            else:
                tooBig = heapq.heappop(self.large)
                self.small.push(tooBig)

    def findMedian(self) -> float:
        if self.small.length() > len(self.large):
            return self.small.top()
        if len(self.large) > self.small.length():
            return self.large[0]
        return (self.small.top() + self.large[0]) / 2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()