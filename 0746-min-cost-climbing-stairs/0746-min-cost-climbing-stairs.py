class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         @cache
#         def climb(i):
#             if i >= len(cost):
#                 return 0
            
#             one = cost[i] + climb(i+1)
#             two = cost[i] + climb(i+2)
#             return min(one, two)
#         return min(climb(0), climb(1))

        dp = collections.defaultdict(int)
        
        i = len(cost) - 1
        
        while i >= 0:
            dp[i] = min(cost[i]+dp[i+1], cost[i]+ dp[i+2])
            i -= 1
        return min(dp[0], dp[1])