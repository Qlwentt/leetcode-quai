class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        seenFirstChar = False
        length = 0
        while i >= 0:
            if s[i] == " ":
                if seenFirstChar:
                    break
                
                    
            else:
                if not seenFirstChar:
                    seenFirstChar = True
                length += 1
            i -= 1
        return length
            