class Solution:
    def maxValue(self, n: str, x: int) -> str:                       
        for i, digit in enumerate(n):
            if digit == "-":
                continue
            if (int(digit) < x and n[0] != "-") or (int(digit) > x and n[0]== "-") :
                return n[:i] + str(x) + n[i:]
        return n + str(x)
            
                    
        
        
        