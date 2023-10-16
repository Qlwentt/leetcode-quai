class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        for i in range(n):
            
            L, R = i, i
            # odd
            while L in range(n) and R in range(n) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
            
            L, R = i, i+1
            # even
            while L in range(n) and R in range(n) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
        return count