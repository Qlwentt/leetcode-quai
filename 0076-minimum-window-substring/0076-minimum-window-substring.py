from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {char: 0 for char in t}
        countS = defaultdict(int)
        
        for char in t:
            countT[char]+= 1
        
        L = 0
        minWindow = float('inf')
        ansL = None
        ansR = None
        for R in range(len(s)):
            countS[s[R]] += 1
            
            while all([countS[char] >= countT[char] for char in countT]):
                if R-L+1 < minWindow:
                    ansL = L
                    ansR = R
                minWindow = min(minWindow, R-L+1)
                countS[s[L]] -= 1
                L += 1
            
        
        return s[ansL:ansR+1] if ansL != None else ""