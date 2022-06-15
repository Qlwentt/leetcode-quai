class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        counts = {}
        longest = 0
        
        while r < len(s):
            count = counts.get(s[r], 0)
            counts[s[r]] = count + 1
            maxFreq = max(counts.values())
            while (r - l + 1) - maxFreq > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest

# O(n) time
# O(26) space (26 letters in the alphabet)