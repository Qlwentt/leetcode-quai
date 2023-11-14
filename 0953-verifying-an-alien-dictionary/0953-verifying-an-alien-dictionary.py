class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def firstDiff(word1,word2):
            for j in range(minLen):
                if word1[j] != word2[j]:
                    return (word1[j], word2[j])
            return "", ""
        
        alienDict = {char: i+1 for i, char in enumerate(order)}
        alienDict[""] = 0
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            
            minLen = min(len(word1), len(word2))
            
            if word1[:minLen] == word2[:minLen] and len(word1) > len(word2):
                return False
            
            diff1,diff2 = firstDiff(word1[:minLen], word2[:minLen])
            if alienDict[diff1] > alienDict[diff2]:
                return False
        return True
            
        
        
                