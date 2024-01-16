from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            hashedWord = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
            for char in word:
                hashedWord[char] += 1
            
            words[hash(tuple(hashedWord.items()))].append(word)
            
        return words.values()