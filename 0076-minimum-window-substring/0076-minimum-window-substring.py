from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        counterS = defaultdict(int)
        counterT = Counter(t)
        
        
        L = 0
        ansL = None
        ansR = None
        minLength = float('inf')
        for R in range(len(s)):
            counterS[s[R]] += 1
            
            while all(counterS[char] >= counterT[char] for char in counterT):
                minLength = min((R - L + 1), minLength)
                if R - L + 1 == minLength:
                    ansL = L
                    ansR = R
                counterS[s[L]] -= 1
                L += 1
        
        return s[ansL:ansR+1] if ansL != None else ""