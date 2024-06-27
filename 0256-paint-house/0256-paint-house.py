class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @cache
        def backtrack(i, prev):
            if i == len(costs):
                return 0
            min_take = float('inf')
            for j in range(len(costs[i])):
                if j != prev:
                    take = costs[i][j] + backtrack(i+1, j)
                    min_take = min(take, min_take)
            return min_take
        
        return backtrack(0, float('inf'))
                    
            
            
        