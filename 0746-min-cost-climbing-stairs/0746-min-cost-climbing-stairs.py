class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def climb(i):
            if i >= len(cost):
                return 0
            
            one = cost[i] + climb(i+1)
            two = cost[i] + climb(i+2)
            return min(one, two)
        return min(climb(0), climb(1))