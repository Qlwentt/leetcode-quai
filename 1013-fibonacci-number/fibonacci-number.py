class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)
# Time: O(2^N)
# Space: O(N)

# Memoization
        # if n <= 1:
        #     return n
        # if n in self.memo:
        #     return self.memo[n]

        # result = self.fib(n-1) + self.fib(n-2)
        # self.memo[n] = result
        # return result

# Time: O(N)
# Space: O(N)
        