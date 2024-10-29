import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    # Max Heap solution
        maxHeap = [-num for num in nums]
        heapify(maxHeap)
        top = None
        for _ in range(k):
            top = heapq.heappop(maxHeap) * -1
            
        return top
    
    # Time: O(K log(n))
    # Space: O(N)
    
    # Min Heap solution
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    # Time: O(N log K)
    # Space: O(K)
    

