from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
     #   {a: e, g:d}
     #   {p:t, a:i, e:l r: e}
        charMap = {}
        
        if len(s) != len(t):
            return false
        
        for i,char in enumerate(s):
            existing = charMap.get(char, t[i])
            if existing != t[i]:
                return False
            charMap[char] = t[i]
                
        return len(charMap.values()) == len(set(charMap.values()))