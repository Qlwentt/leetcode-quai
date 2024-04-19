class Solution:
    def minInsertions(self, s: str) -> int:
        
        i = 0
        balance = 0
        add = 0
        while i < len(s):
            char = s[i]
            if char == "(":
                balance += 2
                i += 1
            else:
                if i + 1 < len(s) and s[i+1] == ")":
                    i += 2
                else:
                    add += 1
                    i += 1
                balance -= 2
                
            if balance < 0:
                add += 1
               
                balance = 0
        return balance + add
        