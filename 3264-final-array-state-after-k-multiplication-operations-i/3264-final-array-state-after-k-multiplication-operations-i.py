class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(num, i) for i, num in enumerate(nums)]
        
        heapq.heapify(min_heap)
        answer = nums
        while k:
            x, i = heapq.heappop(min_heap)
            answer[i] = x * multiplier
            heapq.heappush(min_heap, (x*multiplier, i))
            k -= 1
        return answer
        