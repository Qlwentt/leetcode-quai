class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        patternToWord = {}
        
        for i in range(len(pattern)):
            letter = pattern[i]
            if letter in patternToWord:
                if words[i] != patternToWord[letter]:
                    return False
            patternToWord[letter] = words[i]
        
        return len(set(patternToWord.values())) == len(patternToWord.values())
            
        
            
        
        