
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapify(maxHeap)
        top = None
        for _ in range(k):
            top = heapq.heappop(maxHeap) * -1
            
        return top
        