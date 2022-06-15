from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = Counter(s1)
        windowSize = len(s1)
        
        l = 0
        r = l + windowSize - 1
        
        while r < len(s2):
            subCount = Counter(s2[l:r+1])
            if s1Counts == subCount:
                return True
            l += 1
            r += 1
        return False

# O(n) time
# O(2 * 26) space