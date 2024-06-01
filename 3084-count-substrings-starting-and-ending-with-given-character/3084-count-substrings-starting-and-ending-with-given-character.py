class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        counts = collections.Counter(s)
        n = counts[c]
        return math.comb(n+1, 2)
        
        