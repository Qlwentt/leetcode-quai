import re
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = re.split(r'(\d*|[a-z]*)', abbr)
        abbr = [item for item in abbr if item != ""]
        print(abbr)
        i = 0
        for item in abbr:
            if item.isnumeric():
                length = int(item)
                if item[0] == "0" or i + length > len(word):
                    return False
            else:
                length = len(item)
                if i + length > len(word) or word[i:i+length] != item:
                    return False
            i += length
        return i == len(word)