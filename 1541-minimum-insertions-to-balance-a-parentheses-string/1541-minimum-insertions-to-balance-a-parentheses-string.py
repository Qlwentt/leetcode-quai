class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0
        i = 0
        add = 0
        "))())("
         
        while i < len(s):
            if s[i] == "(":
                balance += 2
                i += 1
            else:
                balance -= 2
                
                if i + 1 in range(len(s)) and s[i+1] == ")":
                    i += 2
                else:
                    i += 1
                    add += 1
                
                if balance < 0:
                    if balance == -2:
                        add += 1
                    else:
                        add += 2
                    balance = 0
        return add + balance
        