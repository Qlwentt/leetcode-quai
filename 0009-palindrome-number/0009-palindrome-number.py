class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        L = 0
        R = len(x) -1
        
        while L < R:
            if x[L] != x[R]:
                return False
            L += 1
            R -= 1
        return True
        