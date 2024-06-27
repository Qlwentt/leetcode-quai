class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2:
            return False
        half = sum_ // 2
        
#         @cache
#         def dp(i, cur_total):
#             if cur_total < 0:
#                 return False
#             if i == len(nums) and cur_total == 0:
#                 return True
#             if i == len(nums):
#                 return False
            
#             take = dp(i+1, cur_total-nums[i])
#             skip = dp(i+1, cur_total)
            
#             return take or skip
#         return dp(0,half)
        n = len(nums)
        dp = collections.defaultdict(lambda:False)
        dp[(n, 0)] = True
        
        for i in range(n-1,-1,-1):
            for cur_total in range(1, half+1):
                take = dp[(i+1, cur_total-nums[i])]
                skip = dp[(i+1, cur_total)]
                dp[(i,cur_total)] = take or skip
        
        return dp[(0,half)]
    
        
        