class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        answer = 0
        for row in bank:
            count = 0
            for char in row:
                if char == "1":
                    count += 1
            answer += prev * count
            if count:
                prev = count
        
        return answer
        
                
        
            
                    
                    
                