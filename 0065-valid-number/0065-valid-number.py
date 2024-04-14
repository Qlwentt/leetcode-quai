class Solution:
    def isNumber(self, s: str) -> bool:
        def isDecimal(num, allowSign=True):
            if not num:
                return False
            if num[0] in "-+":
                if allowSign:
                    return isDecimal(num[1:], False)
                else:
                    return False
            i = num.find(".")
            if i == -1:
                return False
            left = num[:i]
            right = num[i+1:]
            if left == "" and right == "":
                return False
            return (left == "" or isInteger(left, False)) and (right == "" or isInteger(right, False))
        
        def isInteger(num, allowSign=True):
            if not num:
                return False
            if num[0] in "-+":
                if allowSign:
                    return isInteger(num[1:], False)
            for char in num:
                if not char.isnumeric():
                    return False
            return True
            
        
        s = s.lower()
        sParts = s.split("e")
        
        if len(sParts) > 2:
            return False
        if len(sParts) == 1:
            return isDecimal(sParts[0]) or isInteger(sParts[0])
        if len(sParts) == 2:
            return (isDecimal(sParts[0]) or isInteger(sParts[0])) and isInteger(sParts[1])
        else:
            return False
        