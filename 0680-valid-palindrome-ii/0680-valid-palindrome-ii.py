class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPal(L,R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True
        
        L = 0
        R = len(s) - 1
        
        while L < R:
            if s[L] != s[R]:
                return isPal(L+1,R) or isPal(L, R-1)
            L += 1
            R -= 1
        return True
        