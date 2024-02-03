class Solution:
    def minInsertions(self, s: str) -> int:
        #"(()))"
        # 22 21 
            
        #"))())("
        # -22 02
        #  0
        
        # ")()"
        # -121
       #   2
    
      # "(()))(()))()())))"
     #    24 2024 20202 0 
     #   4
    
        balance = 0
        add = 0
        i = 0
        
        while i < len(s):
            char = s[i]
            if char == "(":
                balance += 2
                i += 1
            else:
                if i + 1 in range(len(s)) and s[i+1] == ")":
                    i += 2
                else:
                    add += 1
                    i += 1
                balance -= 2
                if balance < 0:
                    if balance == -2:
                        add += 1
                    else:
                        add += 2
                    balance = 0
                    
        return balance + add