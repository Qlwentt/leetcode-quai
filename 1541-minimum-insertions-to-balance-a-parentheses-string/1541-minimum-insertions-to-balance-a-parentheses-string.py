class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0
        add = 0
        i = 0
        
        while i < len(s):
            char = s[i]
            if char == "(":
                balance += 2
                i += 1
            else:
                balance -= 2
                if i + 1 not in range(len(s)) or s[i+1] != ")":
                    add += 1
                    i += 1
                else:
                    i += 2
                
                if balance < 0:
                    if balance == -1:
                        add += 2
                    else: # balance == -2
                        add += 1
                    balance = 0
        return balance + add