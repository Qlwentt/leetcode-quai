class Solution:
    def maxValue(self, n: str, x: int) -> str:         
        n = list(n)
        
        def get_max(n, is_negative=False):
            for i, digit in enumerate(n):
                if int(digit) < x and not is_negative:
                    return i
                elif int(digit) > x and is_negative:
                    return i + 1
            return len(n) + is_negative
            
                    
        
        if n[0] == "-":
            i = get_max(n[1:], True)
            
        else:
            i = get_max(n)
        n.insert(i, str(x)) 
        return "".join(n)
        
        