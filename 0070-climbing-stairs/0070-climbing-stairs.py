class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.lru_cache
        def fib(n):
            if n <= 1:
                return n
            return fib(n-1) + fib(n-2)
        return fib(n+1)
        