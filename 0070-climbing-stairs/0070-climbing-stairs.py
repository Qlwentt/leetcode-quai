class Solution:
    def climbStairs(self, n: int) -> int:
        1,2,3,5,8,13
        # def climb(n):
        #     if n <= 2:
        #         return n
        #     return climb(n-1) + climb(n-2)
        # return climb(n)
        
        dp = {}
        dp[1] = 1
        dp[2] = 2
        
        i = 3
        
        while i < n + 1:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        
        return dp[n]
            