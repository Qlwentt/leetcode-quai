class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = 0
        both = s + t
        for char in both:
            answer ^= ord(char)
        
        return chr(answer)