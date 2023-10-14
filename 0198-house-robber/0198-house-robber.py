class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        dp[n-1] = nums[n-1]
        
        i = n - 2
        while i >= 0:
            dp[i] = max(nums[i] + dp[i+2], nums[i+1] +dp[i+3])
            i -= 1
        return dp[0]
        