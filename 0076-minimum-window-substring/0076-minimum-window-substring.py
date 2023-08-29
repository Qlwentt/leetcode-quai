from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len (s):
            return ""
        
        counterT = {}
        for char in t:
            counterT[char] = counterT.get(char,0) + 1
        
        counterS = {char:0 for char in counterT.keys()}
        
        minLen = float("inf")
        pos = (None, None)
        
        L = 0
        R = 0
        
        while R < len(s):
            curChar = s[R]
            if curChar in counterS:
                counterS[curChar] += 1
                
            while all(counterS[key] >= counterT[key] for key in counterS.keys()):    
                if R - L + 1 < minLen: # 6 < inf, 10 < 6, 8 < 6, 7 < 6, 6 < 6, 7 < 6, 6 < 6, 5 < 6 4 < 5
                    pos = (L,R) # (0, 5),(8,12), (9, 12)
                    minLen = (R - L + 1) # 6 5 4
                prevChar = s[L]
                if prevChar in counterS:
                    counterS[prevChar] -= 1
                L += 1
            R += 1   
        return s[pos[0]:pos[1]+1] if minLen < float("inf") else ""
   # counterS = {A:0 1 0 1, B:0 1 2 1, C:0 1 0 1} counterT = {A:1,B:1,C:1}    
            
        
        "A D O B E C O D E B A N C"
    #                        L
    #                               R
        