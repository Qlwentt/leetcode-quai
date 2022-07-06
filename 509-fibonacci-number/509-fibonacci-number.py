class Solution:
    def __init__(self):
        self.memo = {} # n -> f(n)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        print(self.memo)
        return self.memo[n]