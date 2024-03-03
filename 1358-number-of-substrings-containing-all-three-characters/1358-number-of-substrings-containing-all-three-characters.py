class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        L = 0
        counts = {"a": 0, "b": 0, "c": 0}
        answer = 0
        for R in range(len(s)):
            counts[s[R]] += 1
            while all(counts[char] >= 1 for char in counts):
                counts[s[L]] -= 1
                answer += len(s) - R 
                L += 1
        return answer