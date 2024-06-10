class Solution:
    def maxValue(self, n: str, x: int) -> str:         
        n = list(n)
        
        def get_max(n, is_negative=False):
            if not is_negative: 
                for i, digit in enumerate(n):
                    if int(digit) < x:
                        return i
                return len(n)
            else:
                for i , digit in enumerate(n):
                    if int(digit) > x:
                        return i + 1
                return len(n) + 1
            
                    
        
        if n[0] == "-":
            i = get_max(n[1:], True)
            
        else:
            i = get_max(n)
        n.insert(i, str(x)) 
        return "".join(n)
        
        