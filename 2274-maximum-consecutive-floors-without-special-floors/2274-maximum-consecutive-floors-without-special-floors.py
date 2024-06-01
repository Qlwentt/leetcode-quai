class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        max_regular = 0
        special = [bottom-1] + special + [top+1]
        special.sort()
        
        for i in range(len(special)-1):
            max_regular = max((special[i+1]-1)-special[i], max_regular)
            
        return max_regular
        
        
        
        