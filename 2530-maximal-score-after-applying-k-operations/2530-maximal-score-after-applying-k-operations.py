class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        score = 0
        while k:
            num = heapq.heappop(max_heap)
            num = -num
            score += num
            
            heapq.heappush(max_heap, -math.ceil(num/3))
            k -= 1
        return score