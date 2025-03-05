from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # count of characters as key in a dictionary, list of words as the value
        words = defaultdict(list)
        for word in strs:
            hashed_word = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
            for char in word:
                hashed_word[char] += 1
            
            words[(tuple(hashed_word.items()))].append(word)
            
        return list(words.values())

        # Time: O(NK) where N is the length of strs and K is the max len of a string in strs
        # Space: O(NK)

        # sorted string is key, array of words is values
        words = defaultdict(list)
        for s in strs:
            words["".join(sorted(s))].append(s)
        return list(words.values())

        # Time: O(NKlogK)
        # Space: O(OK)