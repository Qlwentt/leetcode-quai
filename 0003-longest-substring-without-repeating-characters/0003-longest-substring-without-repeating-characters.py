class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"
        #  L  R
        l = 0
        window = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(r-l+1,longest)
        return longest
        