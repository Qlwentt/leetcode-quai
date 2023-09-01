class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(" ")
        pattern = list(pattern)
        
        if len(pattern) != len(strs):
            return False
        
        patternMap = {}
        for char, word in zip(pattern, strs):
            mappedWord = patternMap.get(char, word)
            if mappedWord != word:
                return False
            patternMap[char] = word
        
        return len(set(patternMap.values())) == len(patternMap.values())
            