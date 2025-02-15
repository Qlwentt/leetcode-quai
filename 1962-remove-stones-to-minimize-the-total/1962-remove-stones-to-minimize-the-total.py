class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        while k != 0:
            greatest = heapq.heappop(max_heap) * -1
            greatest -= int(greatest/2)
            heapq.heappush(max_heap, -greatest)
            k -= 1
            
        return -sum(max_heap)
    
    # Time: O(Klog(N))
    # Space: O(N)