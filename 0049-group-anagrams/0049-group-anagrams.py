from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            hashedWord = { char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
            for char in s:
                hashedWord[char] += 1
            anagrams[hash(tuple(hashedWord.items()))].append(s)
        return anagrams.values()