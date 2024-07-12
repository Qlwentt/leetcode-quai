class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        letter_dict = collections.defaultdict(int)
        L = 0
        for R in range(len(s)):
            letter_dict[s[R]] += 1
            if R-L+1 > 3:
                letter_dict[s[L]] -= 1
                if letter_dict[s[L]] == 0:
                    del letter_dict[s[L]]
                L += 1
            if len(letter_dict) == 3:
                count += 1
        return count