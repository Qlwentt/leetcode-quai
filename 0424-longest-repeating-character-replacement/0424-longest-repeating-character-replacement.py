class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        longest = 0
        l = 0
       # "ABCDE"
      #  L
      #  R
        for r in range(len(s)):
            counts[s[r]] += 1
            target = max(counts, key=counts.get)
            while (r-l+1)-counts[target] > k:
                counts[s[l]] -= 1
                target = max(counts, key=counts.get)
                l += 1
            longest = max(longest, r-l+1)
        return longest
                
        