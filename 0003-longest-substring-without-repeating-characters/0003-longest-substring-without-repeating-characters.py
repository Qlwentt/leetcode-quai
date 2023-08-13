class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        L = 0
        seen = set()
        for R in range(len(s)):
            if s[R] not in seen:
                longest = max(longest, R-L+1)
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
        return longest
            
        