class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-x for x in stones]
        heapq.heapify(stoneHeap)
        while len(stoneHeap) > 1:
            y = heapq.heappop(stoneHeap)
            x = heapq.heappop(stoneHeap)
                        
            y = y - x
            if y:
                heapq.heappush(stoneHeap, y)
        
        return abs(stoneHeap[0]) if stoneHeap else 0