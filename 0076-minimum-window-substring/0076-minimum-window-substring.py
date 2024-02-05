class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        counterS = defaultdict(int)
        counterT = defaultdict(int)
        
        for char in t:
            counterT[char] += 1
        
        L = 0
        answerL = None
        answerR = None
        minLen = float('inf')
        for R in range(len(s)):
            char = s[R]
            counterS[char] += 1
            
            while all(counterS[key] >= counterT[key] for key in counterT.keys()):
                minLen = min(R-L+1, minLen)
                if R-L+1 == minLen:
                    answerL = L
                    answerR = R
                removingChar = s[L]
                counterS[removingChar] -= 1
                L += 1
        print (answerL)
        return s[answerL:answerR+1] if answerL is not None else ""
        