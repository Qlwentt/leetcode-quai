class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ' '.join(words)
        res = []
        for w in words:
            if s.count(w) > 1:
                res.append(w)
        return res

     