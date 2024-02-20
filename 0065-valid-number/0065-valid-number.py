class Solution:
    def isNumber(self, s: str) -> bool:
        noNeg = re.sub(r"(\+|\-)", "", s)
        if noNeg.isalpha():
            return False
        try:
            num = float(s)
        except ValueError:
            return False
        
        return True
            
        