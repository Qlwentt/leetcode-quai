class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        subtractMap = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
        
        i = 0
        num = 0
        while i < len(s):
            char = s[i]
            if char in subtractMap:
                if i + 1 < len(s) and s[i+1] in subtractMap[char]:
                    num += romanMap[s[i+1]] - romanMap[char]
                    i += 2
                else:
                    num += romanMap[char]
                    i += 1
            else:
                num += romanMap[char]
                i += 1
        
        return num
            
        