class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n == 0:
                return 1

            answer = 1
            while n:
                if n % 2:
                    answer = answer * x
                    n -= 1
                else:
                    x = x * x
                    n = n // 2

            return answer
        if n < 0:
            return 1/power(x,-n)
        else:
            return power(x,n)
            
        