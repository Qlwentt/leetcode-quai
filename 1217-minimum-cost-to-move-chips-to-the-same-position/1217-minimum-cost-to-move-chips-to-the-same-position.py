class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counts = {0:0, 1:0}
        for num in position:
            counts[num%2] += 1
        
        return min(counts.values())