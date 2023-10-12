class Solution:
    def rob(self, nums: List[int]) -> int:
        # recursion
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 0:
        #     return 0
        # return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))
    
        # memoization
#         memo = {}
#         def robRecursive(i):
#             if i == len(nums)-1:
#                 return nums[i]
#             if i >= len(nums):
#                 return 0
#             if i in memo:
#                 return memo[i]

#             memo[i] = max(nums[i] + robRecursive(i+2), nums[i+1] + robRecursive(i+3))
#             return memo[i]
#         return robRecursive(0)
    
        # dp 
        def robDp():
            n = len(nums)
            dp = [0] * n
            dp[n-1] = nums[n-1]
            [0,0,0,0,1]
            i = n -1
            while i >= 0:
                nextHouse1 = dp[i+2] if i+2 in range(n) else 0
                nextHouse2 = dp[i+3] if i+3 in range(n) else 0
                nextNum = nums[i+1] if i+1 in range(n) else 0
                dp[i] = max(nums[i] + nextHouse1, nextNum + nextHouse2)
                i -= 1
            
            return dp[0]
        
        return robDp()
            
    
        