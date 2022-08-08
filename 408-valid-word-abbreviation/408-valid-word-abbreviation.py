import re
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = re.split('(\d+)', abbr)
        for i, part in enumerate(abbr):
            if i < len(abbr) - 1 and part.isdigit() and abbr[i+1].isdigit():
                return False
            if part.isdigit() and part[0] == "0":
                return False
    
        i = 0
        for part in abbr:
            if part.isdigit():
                i += int(part)
            else:
                for char in part:
                    if i >= len(word):
                        return False
                    if word[i] != char:
                        return False
                    i += 1
        
                    
        return i == len(word)
                    