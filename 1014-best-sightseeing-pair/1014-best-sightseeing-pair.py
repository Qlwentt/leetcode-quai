class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        @cache
        def dp(i, num_chosen):
            if num_chosen == 2:
                return 0
            if i == len(values):
                return float("-inf")
            
            position = i if num_chosen == 0 else -i
            pick = values[i] + position + dp(i+1,num_chosen+1)
            skip = dp(i+1,num_chosen)
            
            return max(pick, skip)
        
        return dp(0,0)
            
            