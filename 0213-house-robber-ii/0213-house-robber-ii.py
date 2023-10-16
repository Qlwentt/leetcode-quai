class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robLine(nums):
            if len(nums) == 1:
                return nums[0]
            n = len(nums)
            dp = [0] * (n+1)
            dp[n-1] = nums[n-1]
            dp[n-2] = max(nums[n-2] , dp[n-1])
            
            i = n - 3
            
            while i >= 0:
                dp[i] = max(nums[i] + dp[i+2], nums[i+1] + dp[i+3])
                i -= 1
            return dp[0]
            
        return max(robLine(nums[1:]), robLine(nums[:-1]))