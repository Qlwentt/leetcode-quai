class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        rows = 0 
        
        while n > 0: # -1
            n -= (rows + 1)
            rows += 1
            
        return rows-1 if n < 0 else rows
        
            