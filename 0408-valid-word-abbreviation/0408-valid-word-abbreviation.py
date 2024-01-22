import re
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = re.split(r"(\d*|[a-z]*)", abbr)
        abbr = [item for item in abbr if item != ""]
        
        i = 0
        
        for item in abbr:
            if item.isnumeric():
                if item[0] == "0" or int(item) + i > len(word):
                    return False
                i += int(item)
            else:
                if i + len(item) > len(word) or word[i:i+len(item)] != item:
                    return False
                i += len(item)
        
        return i == len(word)