class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = nums
        heapq.heapify(min_heap)
        answer = 0
        while min_heap:
            
            a = heapq.heappop(min_heap)
            b = heapq.heappop(min_heap) if min_heap else k
            if a >= k and b >= k:
                break
            answer += 1
            min_ = min(a,b)
            max_ = max(a,b)
            c = min_ * 2 + max_
            heapq.heappush(min_heap, c)
        return answer
        