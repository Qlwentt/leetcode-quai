class Solution:
    def rob(self, nums: List[int]) -> int:
#         @cache
#         def helper(i):
#             if i >= len(nums):
#                 return 0
            
#             take = nums[i] + helper(i+2)
#             skip = helper(i+1)
#             return max(take, skip)
#         return helper(0)
        dp = collections.defaultdict(int)
    
        for i in range(len(nums)-1,-1,-1):
            take = nums[i] + dp[i+2]
            skip = dp[i+1]
            dp[i] = max(take, skip)
            
        return dp[0]
        
    
    
        