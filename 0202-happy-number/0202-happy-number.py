class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(n):
            result = 0
            while n:
                digit = n % 10
                result += digit ** 2
                n = n // 10
            return result
        slow = n
        fast = n
        
        while slow:
            slow = sumSquares(slow)
            fast = sumSquares(sumSquares(fast))
            if fast == slow:
                return fast == 1
        
        
            
        