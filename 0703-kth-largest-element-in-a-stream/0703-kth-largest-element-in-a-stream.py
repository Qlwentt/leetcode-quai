class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = nums
        heapq.heapify(self.store)
        self.k = k
        
        while len(self.store) > self.k:
            heapq.heappop(self.store)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.store, val)
        
        while len(self.store) > self.k:
            heapq.heappop(self.store)
            
        return self.store[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)