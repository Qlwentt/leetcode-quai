class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxSize = 0
        seen = set()
        size = 0

        while r < len(s):
            size += 1
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                size -= 1
            seen.add(s[r])
            maxSize = max(size, maxSize)
            r+= 1
        return maxSize