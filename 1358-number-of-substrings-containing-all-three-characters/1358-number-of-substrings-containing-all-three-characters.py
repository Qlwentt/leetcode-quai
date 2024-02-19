class Solution:
    def numberOfSubstrings(self, s: str) -> int:
    #    "abcabc"
      #   L
      #     R
        counts = {"a": 0, "b": 0, "c": 0}
        L = 0
        answer = 0
        for R in range(len(s)):
            counts[s[R]] += 1
            while all([value >= 1 for value in counts.values()]):
                answer += len(s) - R
                counts[s[L]] -= 1
                L += 1
        return answer