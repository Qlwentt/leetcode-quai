class Solution:
    def climbStairs(self, n: int) -> int:
        
        def fib(n):
            if n <= 1:
                return n

            nMinus1 = 1
            nMinus2 = 0
            
            while n > 1 :
                fibN = nMinus1 + nMinus2
                nMinus1, nMinus2 = fibN, nMinus1
                n -= 1
            
            return fibN
                
        
        
        return fib(n+1)