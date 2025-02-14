class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = 0
        
        for char in s:
            answer ^= ord(char)

        for char in t:
            answer ^= ord(char)
        
        return chr(answer)