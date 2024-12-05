class Solution:
    def canChange(self, start: str, target: str) -> bool:
        p1 = 0
        p2 = 0
     
        start_count = collections.Counter(start)
        target_count = collections.Counter(target)
        
        while p1 < len(start):
            if start[p1] == "L":
                
                if p2 == len(start) or target[p2] == "R":
                    return False
                else:
                    if target[p2] != "L":
                        p2 += 1
                    else:
                        if p1 < p2:
                            return False
                        else:
                            p1 += 1
                            
                            p2 += 1
            elif start[p1] == "R":
                if p2 == len(start) or target[p2] == "L":
                    return False
               
                else:
                    
                    if target[p2] != "R":
                        p2 += 1
                    else:
                        if p2 < p1:
                            return False
                        else:
                            
                            p1 += 1
                            p2 += 1
                    print(p1,p2)
            else:
                p1 += 1
                
        return start_count["L"] == target_count["L"] and start_count["R"] == target_count["R"]
       
                        
        
                