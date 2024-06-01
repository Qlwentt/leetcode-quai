class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        answer = 0
        seen = 0
        for char in s:
            if char == c:
                seen += 1
                answer += seen
        
        return answer
        
        