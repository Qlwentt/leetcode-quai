class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(n):
            if n == 1:
                return 1
            
            max_product = float('-inf')
            for i in range(1,n):
                product = i * dp(n-i)
                max_product = max(product, i * (n-i) , max_product)
                
            return max_product
        
        return dp(n)