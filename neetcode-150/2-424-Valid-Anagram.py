class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        
        for letter in s:
            count = sDict.get(letter, 0)
            sDict[letter] = count + 1
            
        for letter in t:
            count = tDict.get(letter, 0)
            tDict[letter] = count + 1
            
        return sDict == tDict

# O(n) time
# O(n) space