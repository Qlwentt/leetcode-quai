class Solution:
    def findScore(self, nums: List[int]) -> int:
        mark = {i:False for i, num in enumerate(nums) }
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        
        score = 0
        
        while min_heap:
            chosen, i = heapq.heappop(min_heap)
            if mark[i]:
                continue
            score += chosen
            if i - 1 in mark:
                mark[i-1] = True
            if i + 1 in mark:
                mark[i+1] = True
        
        return score
        