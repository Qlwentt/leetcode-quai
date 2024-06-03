class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def isPali(n,base):
            conversion = []
            
            while n:
                conversion.append(n%base)
                n = n // base
                
            return conversion == conversion[::-1]
            
        for base in range(2, n-1):
            if not isPali(n, base):
                return False
        
        return True