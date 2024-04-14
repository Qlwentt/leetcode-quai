class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        add = 0
        
        for char in s:
            if char == "(":
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                add += 1
                balance = 0
        return add + balance 
        