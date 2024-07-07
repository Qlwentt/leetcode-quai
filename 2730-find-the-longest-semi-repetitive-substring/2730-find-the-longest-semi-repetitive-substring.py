class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        L = 0
        repeats = 0
        prev = 0
        longest = 0
        for R in range(len(s)):
            if prev and prev == s[R]:
                repeats += 1
            prev = s[R]
            while repeats > 1:
                repeats -= 1 if s[L] == s[L+1] else 0
                L += 1
            longest = max(longest, R-L+1)
        return longest