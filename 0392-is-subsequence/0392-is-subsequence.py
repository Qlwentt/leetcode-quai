class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pS = 0
        pT = 0
        
        while pS < len(s) and pT < len(t):
            if s[pS] == t[pT]:
                pS += 1
                pT += 1
            else:
                pT += 1
        
        return pS == len(s)
        
        
        