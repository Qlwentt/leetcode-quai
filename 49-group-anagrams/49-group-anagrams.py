from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabetDict = {}
        for i, letter in enumerate(alphabet):
            alphabetDict[letter] = i
        
        anagrams = defaultdict(list)
        for word in strs:
            encoded = [0] *26
            for letter in word:
                encoded[alphabetDict[letter]] += 1
            anagrams[tuple(encoded)].append(word)
        return anagrams.values()
        