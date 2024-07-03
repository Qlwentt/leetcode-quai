class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_set = set()
        pairs = 0
        for word in words:
            reversed_word = word[::-1]
            if reversed_word in word_set:
                pairs += 1
                word_set.remove(reversed_word)
            else:
                word_set.add(word)
                
        return pairs