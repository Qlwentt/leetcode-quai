
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        
        minCost = 0
        for i, price in enumerate(cost):
            if (i+1) % 3 != 0:
                minCost += price
        return minCost
            
        