class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        maxLength = 0
        
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            length = r - l + 1
            maxLength = max(length, maxLength)
            seen.add(s[r])
            r += 1
        return maxLength
# O(n) time
# O(26) space (26 letters in alphabet)