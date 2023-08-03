class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        
        if len(s) > len(t):
            return False
        
        while p1 < len(s) and p2 < len(t):
            sChar = s[p1]
            tChar = t[p2]
            
            if sChar == tChar:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1 == len(s)
        