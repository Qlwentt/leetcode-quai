class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0
        add = 0
        
        for char in s:
            if char == "(":
                bal += 1
            else: # char == )
                bal -= 1
            if bal < 0:
                add += 1
                bal = 0
        
        return add + bal
    
# Time: O(N) iterate through string once
# Space O(1) only use int vars