import heapq
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        maxHeap = [-candy for candy in cost]
        heapify(maxHeap)
        minCost = 0
      
        while len(maxHeap) >= 2:
            candy1 = heappop(maxHeap) * -1
            candy2 = heappop(maxHeap) * -1

            minCost += candy1 + candy2
            if maxHeap:
                rejectedCandies = []
                while maxHeap:
                    freeCandy = heappop(maxHeap) * -1
                    if freeCandy <= candy1 + candy2:
                        break
                    else:
                        rejectedCandies.append(freeCandy * -1)
                while rejectedCandies:
                    heappush(maxHeap, rejectedCandies.pop())
        if maxHeap:
            minCost += heappop(maxHeap) * -1
        
        return minCost
            
        