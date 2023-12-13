class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            s, t = t, s
        p = 0
        q = 0
        while p < len(s):
            sChar = s[p]
            tChar = t[q] if q in range(len(t)) else ""
            if sChar != tChar:
                replace = s[p+1:] == t[q+1:] 
                delete = s[:p] + s[p+1:] == t
                return replace or delete
            p += 1
            q += 1
        return False
            
        
        
        # "ac"
        #   P
        # "a"
        #   Q