class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = [-happy for happy in happiness]
        heapq.heapify(max_heap)
        
        decrementer = 0
        answer = 0
        while max_heap and k:
            child = heapq.heappop(max_heap) * -1
            child -= decrementer
            child = max(0, child)
            decrementer += 1
            answer += child
            k -= 1
        
        return answer
        
        