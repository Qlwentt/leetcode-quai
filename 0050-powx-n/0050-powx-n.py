class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            halfpower = power(x, n//2)
            if n % 2:
                return halfpower * halfpower * x
            return halfpower * halfpower
        if n < 0:
            return 1/power(x,-n)
        else:
            return power(x,n)
        