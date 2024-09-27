class Solution:
    def myPow(self, x: float, n: int) -> float:      
        def power(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            half = power(x, n // 2)
            if n % 2: # odd
                return half * half * x
            else: # even
                return half * half
        
        if n < 0:
            return 1/power(x,-n)
        else:
            return power(x,n)

        
        
# Time: O(log(N)) (because halfing every time)
# Space: O(log(N))
        
        
        
       