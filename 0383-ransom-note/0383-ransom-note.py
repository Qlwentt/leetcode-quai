from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        for char in ransomNote:
            if char in magazine and magazine[char] > 0:
                magazine[char] -= 1
            else:
                return False
        
        return True