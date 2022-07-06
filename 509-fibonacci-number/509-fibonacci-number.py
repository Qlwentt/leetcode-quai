class Solution:
#     def __init__(self):
#         self.memo = {} # n -> f(n)
    
#     def fib(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return n
#         if n not in self.memo:
#             self.memo[n] = self.fib(n-1) + self.fib(n-2)
#         print(self.memo)
#         return self.memo[n]
    def fib(self, n):
        fib1 = 0
        fib2 = 1
        
        if n <= 1:
            return n
        
        i = 0
        while i < n -1:
            i += 1
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
        return fib