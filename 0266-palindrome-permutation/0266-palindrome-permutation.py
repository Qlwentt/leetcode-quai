from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charDict = defaultdict(lambda: False)
        
        for char in s:
            charDict[char] = not charDict[char]
        
        return sum(charDict.values()) <= 1