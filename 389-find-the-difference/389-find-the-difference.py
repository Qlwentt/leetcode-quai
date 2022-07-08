from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = Counter(s)
        tCount = Counter(t)
        
        for letter in tCount:
            if sCount[letter] != tCount[letter]:
                return letter