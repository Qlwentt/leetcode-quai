from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque([])
        
        doms = list(dominoes)
        
        for i, d in enumerate(doms):
            if d != ".":
                q.append((i,d))
                
        while q:
            i, d = q.popleft()
            
            if d == "L":
                if i - 1 in range(len(doms)) and doms[i-1] == ".":                    
                    doms[i-1] = "L"
                    q.append((i-1,"L"))
            else:
                if i + 1 in range(len(doms)) and doms[i+1] == ".":
                    # knock over unless L is holding it up
                    if i + 2 in range(len(doms)) and doms[i+2] == "L":
                        q.popleft()
                        continue
                    doms[i+1] = "R"
                    q.append((i+1, "R"))
                    
        return "".join(doms)
        