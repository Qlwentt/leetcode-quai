class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        L = 0
        counts = {"a": 0, "b": 0, "c": 0}
        answer = 0
        for R in range(len(s)):
            char = s[R]
            counts[char] += 1
            while all([count >= 1 for char, count in counts.items()]):
                answer += len(s) - R
                counts[s[L]] -= 1
                L += 1
        return answer