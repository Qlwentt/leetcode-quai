class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        #"egcfe"
        #  L R
        L = 0
        R = len(s) - 1
        
        answer = list(s)
        
        while L < R:
            if s[L] != s[R]:
                numL = ord(s[L])
                numR = ord(s[R])
            
                if numL < numR:
                    answer[R] = s[L]
                else:
                    answer[L] = s[R]
            L += 1
            R -= 1
        return "".join(answer)