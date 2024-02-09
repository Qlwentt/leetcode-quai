class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = re.split(r'(\d+)', abbr)
        abbr = [item for item in abbr if item != ""]
        p1 = 0
        p2 = 0
        
        while p2 < len(abbr):
            if abbr[p2].isnumeric():
                charLen = int(abbr[p2])
                if not p1+charLen-1 in range(len(word)) or abbr[p2][0] == "0":
                    return False           
            else:
                charLen = len(abbr[p2])
                if not p1+charLen-1 in range(len(word)) or word[p1:p1+charLen] != abbr[p2]:
                    return False
            p1 += charLen
            p2 += 1
        return p1 == len(word)