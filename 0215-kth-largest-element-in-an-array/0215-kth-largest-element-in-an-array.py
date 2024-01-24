
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapify(maxHeap)
        for _ in range(k-1):
            heapq.heappop(maxHeap)
            
        return -maxHeap[0]
        