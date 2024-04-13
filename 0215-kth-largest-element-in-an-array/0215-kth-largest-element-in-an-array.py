import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # - sorting; time: O(NlogN), space: O(N)
        # - max heap, pop k times; time: (KlogN), space: O(N)
        # - min heap of k size; time(NlogK), space: O(K)
        # - quick select; time: aver - O(N). worst: O(N^2), space: O(N)

#         maxHeap = [-num for num in nums]
#         heapify(maxHeap)
        
#         while k:
#             answer = heappop(maxHeap)
#             k -= 1
#         return -answer

        minHeap = []
        for num in nums:
            heappush(minHeap,num)
            if len(minHeap) > k:
                heappop(minHeap)
        
        return minHeap[0]
        
        