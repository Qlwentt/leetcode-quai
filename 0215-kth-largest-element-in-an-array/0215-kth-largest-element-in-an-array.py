import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # - sorting
        # - max heap, pop k times
        # - min heap of k size
        # - quick select
        maxHeap = [-num for num in nums]
        heapify(maxHeap)
        
        while k:
            answer = heappop(maxHeap)
            k -= 1
        return -answer
        
        