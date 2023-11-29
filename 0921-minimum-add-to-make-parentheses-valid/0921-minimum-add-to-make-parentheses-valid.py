class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        add = 0 
        bal = 0 
        
        for char in s:
            if char == "(":
                bal += 1
            elif char == ")":
                bal -= 1
            if bal < 0:
                add += 1
                bal = 0
        return bal + add 