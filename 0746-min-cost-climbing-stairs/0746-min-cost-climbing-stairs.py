class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
# recursive
#         def climb(i, curCost):
#             if i >= len(cost) - 2:
#                 nextCost = cost[i+1] if i+1 in range(len(cost)) else 0
#                 curCost += min(cost[i], nextCost)
#                 return curCost
            
#             return min(climb(i+1, curCost+cost[i]), climb(i+2,curCost + cost[i+1]))
#         return climb(0, 0)

# memoization
#         memo = {}
#         def climb(i):
#             if i >= len(cost) - 2:
#                 nextCost = cost[i+1] if i+1 in range(len(cost)) else 0
#                 minCost = min(cost[i], nextCost)
#                 return minCost
#             if i in memo:
#                 return memo[i]
#             memo[i] = min(cost[i] + climb(i+1), cost[i+1] + climb(i+2))
#             return memo[i]
        
#         return climb(0)

# # dp
        def climb():
            n = len(cost)

            dp = [-1]*n
            dp[n-2] = min(cost[n-2], cost[n-1]) 
            dp[n-1] = min(cost[n-1], 0)
            
            i = n-3
            while i >= 0:
                dp[i] = min(cost[i] + dp[i+1], cost[i+1] + dp[i+2])
                i -= 1
            return dp[0]
        return climb()
        
        