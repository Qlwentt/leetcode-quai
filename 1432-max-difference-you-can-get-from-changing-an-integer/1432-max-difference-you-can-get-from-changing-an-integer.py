class Solution:
    def maxDiff(self, num: int) -> int:
        high = str(num) 
        low = str(num)
        x1 = "9"
        
        for i, char in enumerate(high):
            if char != "9":
                x1 = char
                break
        x2 = "1"
        found = False
        for i, char in enumerate(low):
            if char != "1" and char != "0":
                x2 = char
                found = True
                break
        high = high.replace(x1, "9")
        low = low.replace(x2, "1" if i == 0 or not found else "0")
        print(high, low)
        return int(high) - int(low)
                
            
                
        
        