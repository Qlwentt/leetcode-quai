class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # @cache
#         def dp(i):
#             if i == len(nums):
#                 return True
            
#             if i + 1 < len(nums) and nums[i] == nums[i+1]:
#                 if dp(i+2):
#                     return True
#                 if i+ 2 < len(nums) and nums[i+1] == nums[i+2]:
#                     if dp(i+3):
#                         return True
#             if i+1 < len(nums) and i+2 < len(nums) and nums[i] + 1 == nums[i+1] and nums[i+1] +1 == nums[i+2]:
#                 if dp(i+3):
#                     return True
#             return False
        
#         return dp(0)
        n = len(nums)
        dp = collections.defaultdict(lambda:False)
        dp[n] = True
        
        for i in range(n-1,-1,-1):
            answer = False
            if i + 1 < n and nums[i] == nums[i+1]:
                answer |= dp[i+2]
                if i + 2 < n and nums[i+1] == nums[i+2]:
                    answer |= dp[i+3]
            if i + 1 < n and i+2 < n and nums[i] + 1 == nums[i+1] and nums[i+1] + 1 == nums[i+2]:
                answer |= dp[i+3]
            dp[i] = answer
        return dp[0]
                
    
    