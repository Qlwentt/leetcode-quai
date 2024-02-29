class Solution:
    def isNumber(self, s: str) -> bool:
        def isDecimal(s):
            if s == "":
                return False
            if s[0] == "-" or s[0]== "+":
                return isDecimal(s[1:])
            s = s.split(".")
            if len(s) != 2:
                return False
            if s[0] == "" and s[1] == "":
                return False
            
            return (isInteger(s[0], True) or s[0] == "")  and (isInteger(s[1], False) or s[1] == "")
        def isInteger(s, canHaveSign):
            if s == "":
                return False
            if s[0] == "-" or s[0] == "+":
                if not canHaveSign:
                    return False
                return isInteger(s[1:], False)
            for i, char in enumerate(s):
                if not char.isdigit():
                    return False  
            return True
        
        s = s.lower()
        splitByE = re.split(r'e', s)
        
        if len(splitByE) > 2:
            return False
        if len(splitByE) == 0:
            return False
        if len(splitByE) == 1 and "e" in s:
            return False
        if len(splitByE) == 1:
            return isDecimal(splitByE[0]) or isInteger(splitByE[0], True)
        # len is 2
        if splitByE[0] == "" or splitByE[1] == "":
            return False
        return (isDecimal(splitByE[0]) or isInteger(splitByE[0], True)) and isInteger(splitByE[1], True)
            
        
        
            
        