class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longS = ""
        
        for i in range(len(s)):
            # odd
            L,R = i, i
            while L in range(len(s)) and R in range(len(s)) and s[L] == s[R]:
                longest = max(longest, R-L+1)
                if longest == (R-L+1):
                    longS = s[L:R+1]
                L -= 1
                R += 1
            
            # even
            L, R = i, i + 1
            while L in range(len(s)) and R in range(len(s)) and s[L] == s[R]:
                longest = max(longest, R-L+1)
                if longest == (R-L+1):
                    longS = s[L:R+1]
                L -= 1
                R += 1
        return longS