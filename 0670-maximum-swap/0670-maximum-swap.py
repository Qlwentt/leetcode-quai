class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        
        last = {digit: i for i, digit in enumerate(s)}
        
        for i, digit in enumerate(s):
            for larger in range(9, int(digit), -1):
                larger = str(larger)
                if larger in last and last[larger] > i:
                    s[i], s[last[larger]] = s[last[larger]] , s[i]
                    return int("".join(s))
        return num
                    
            
        
        
        