class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dp(n):
            if n == 0:
                return n
            if n < 0:
                return float('inf')
           
            min_numbers = float('inf')
            for i in range(1,int(math.sqrt(n))+1):
                if i * i <= n:
                    use_i = 1 + dp(n-(i*i)) 
                    min_numbers = min(use_i, min_numbers)
            return min_numbers
        return dp(n)
        