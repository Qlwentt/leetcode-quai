from functools import lru_cache
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        @lru_cache
        def wordInS(word,s):
            p1 = 0 # for s
            p2 = 0 # for word

            if len(word) > len(s):
                return False

            while p2 < len(word) and p1 < len(s):
                if s[p1] != word[p2]:
                    p1 += 1
                else:
                    p1 += 1
                    p2 += 1

            if p1 >= len(s) and p2 < len(word):
                return False
            return True

        count = 0
        for word in words:
            if wordInS(word,s):
                count += 1
        return count   