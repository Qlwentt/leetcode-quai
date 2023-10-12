class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def fib(n):
            if n <= 1:
                return n
            if n in cache:
                return cache[n]
            cache[n] = fib(n-1) + fib(n-2)
            return cache[n]
        return fib(n+1)
        