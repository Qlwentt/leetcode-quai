class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        letter_dict = collections.defaultdict(int)
        L = 0
        for R in range(len(s)):
            if R-L+1 > 3:
                letter_dict[s[L]] -= 1
                if letter_dict[s[L]] == 0:
                    del letter_dict[s[L]]
                L += 1
            letter_dict[s[R]] += 1
            if len(letter_dict) == 3:
                count += 1
        return count
    
# Time: O(N)
# Space: O(K) where K is 3 -- so essentially O(1)