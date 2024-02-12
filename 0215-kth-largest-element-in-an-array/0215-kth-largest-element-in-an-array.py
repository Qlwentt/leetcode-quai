class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap =[-num for num in nums]
        heapq.heapify(maxHeap)
        
        while k:
            answer = -heapq.heappop(maxHeap)
            
            k -= 1
            
        return answer
        