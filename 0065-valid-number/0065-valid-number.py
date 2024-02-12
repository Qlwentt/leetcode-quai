class Solution:
    def isNumber(self, s: str) -> bool:
        noSign = re.sub(r'(\+|\-)', "", s)
        if noSign.isalpha():
            return False
        
        try:
            float(s)
        except ValueError:
            return False
        
        return True