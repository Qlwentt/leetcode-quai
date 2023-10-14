class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n <= 1:
                return n
            
            dp = [0] * (n+1)
            dp[1] = 1
            
            i = 2
            while i <= n:
                dp[i] = dp[i-1] + dp[i-2]
                i += 1         
            return dp[n]
        return fib(n+1)