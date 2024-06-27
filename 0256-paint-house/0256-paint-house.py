class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
#         @cache
#         def dp(i, prev):
#             if i == len(costs):
#                 return 0
#             min_take = float('inf')
#             for j in range(len(costs[i])):
#                 if j != prev:
#                     take = costs[i][j] + dp(i+1, j)
#                     min_take = min(take, min_take)
#             return min_take
        
#         return dp(0, float('inf'))

        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        for i in range(len(costs)-1,-1,-1):
            for prev in range(len(costs[i])):
                min_take = float('inf')
                for j in range(len(costs[i])):
                    if j != prev:
                        take = costs[i][j] + dp[i+1][j]
                        min_take = min(take, min_take) 
                dp[i][prev] = min_take
                
        return min(dp[0].values())
    
        
    
        
                    
            
            
        