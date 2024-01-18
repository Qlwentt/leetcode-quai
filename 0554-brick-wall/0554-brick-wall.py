class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGaps = {0:0}
        
        for row in wall:
            total = 0
            for brickLen in row[:-1]:
                total += brickLen
                countGaps[total] = countGaps.get(total, 0) + 1
        return len(wall) - max(countGaps.values())
                
            
            
                
            
        
        