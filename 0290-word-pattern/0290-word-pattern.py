class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        patternToWord = {}
        wordToPattern = {}
        
        for i in range(len(pattern)):
            letter = pattern[i]
            if letter in patternToWord:
                if words[i] != patternToWord[letter]:
                    return False
            patternToWord[letter] = words[i]
            
        for i in range(len(pattern)):
            word = words[i]
            if word in wordToPattern:
                if pattern[i] != wordToPattern[word]:
                    return False
            wordToPattern[word] = pattern[i]
        
        return True
            
        
            
        
        