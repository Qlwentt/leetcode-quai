class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        counts = collections.Counter(s)
        n = counts[c]
        answer = 0
        while n:
            answer += n
            n -= 1
        return answer
        
        