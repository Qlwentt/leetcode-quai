class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = re.split(r'(\d+)', abbr)
        abbr = [item for item in abbr if item != ""]
        
        p1 = 0
        
        for p2 in range(len(abbr)):
            if abbr[p2].isnumeric():
                length = int(abbr[p2])
                if abbr[p2][0] == "0" or p1 + length - 1 not in range(len(word)):
                    return False
            else:
                length = len(abbr[p2])
                if p1 + length -1 not in range(len(word)) or word[p1:p1+length] != abbr[p2]:
                    return False
            p1 += length
        return p1 == len(word)
        