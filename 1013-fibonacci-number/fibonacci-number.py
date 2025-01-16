class Solution:
    memo = {}
# Brute Force - Recursion
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)
# # Time: O(2^N)
# # Space: O(N)

# # Dynamic Programming - Top Down - Memoization
        if n <= 1:
            return n
        if n in self.memo:
            return self.memo[n]

        result = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = result
        return result

# Time: O(N)
# Space: O(N)

# Dynamic Programming - Bottom-Up - Tabulation

        if n <= 1:
            return n
        
        dp = [0] * (n+1) # set up dp array
        dp[1] = 1 # "base case"
        for x in range(2,n+1):
            dp[x] = dp[x-1] + dp[x-2] # "recursive case"
        
        return dp[n] # return result

# Time: O(N)
# Space: O(N)

# Dynamic Programming - Bottom-Up Tabulation - Space Optimized
        if n <= 1:
            return n
        
        n_minus_2 = 0
        n_minus_1 = 1
        fn = 0
        for _ in range(2, n+1):
            fn = n_minus_2 + n_minus_1 
            n_minus_1, n_minus_2 = fn, n_minus_1
        return fn
# Time: O(N)
# Space: O(1)
