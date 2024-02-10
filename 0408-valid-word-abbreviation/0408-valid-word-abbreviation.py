class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = re.split(r'(\d+)', abbr)
        abbr = [item for item in abbr if item != ""]
        
        p1 = 0
        for p2 in range(len(abbr)):
            if abbr[p2].isnumeric():
                charLen = int(abbr[p2])
                if p1 + charLen -1 not in range(len(word)) or abbr[p2][0] == "0":
                    return False
            else:
                charLen = len(abbr[p2])
                if p1 + charLen - 1 not in range(len(word)) or word[p1:p1+charLen] != abbr[p2]:
                    return False
            
            p1 += charLen
            
        return p1 == len(word)