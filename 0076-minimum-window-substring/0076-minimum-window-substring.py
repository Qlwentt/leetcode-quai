from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        counterT = Counter(t)
        counterS = defaultdict(int)
        
        L = 0
        minLen = len(s) + 1
        ansL = None
        ansR = None
        for R in range(len(s)):
            char = s[R]
            counterS[char] += 1
            while all([counterS[char] >= counterT[char] for char in counterT]):
                if R - L + 1 < minLen:
                    ansL = L
                    ansR = R
                minLen = min(minLen, R - L + 1)
                counterS[s[L]] -= 1
                L += 1
                
        return s[ansL:ansR+1] if ansL != None else ""