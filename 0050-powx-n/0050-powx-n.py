class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1
            
            halfpower = power(x, n // 2)
            if n % 2:
                return x * halfpower * halfpower
            else:
                return halfpower * halfpower
            
        if n < 0:
            return 1/power(x, -n)
        else:
            return power(x,n)