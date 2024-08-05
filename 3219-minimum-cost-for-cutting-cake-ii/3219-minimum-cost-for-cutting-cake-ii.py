class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        h = 0
        v = 0
        
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        cost = 0
        while h < len(horizontalCut) or v < len(verticalCut):
            cutH = horizontalCut[h] if h in range(len(horizontalCut)) else float('-inf')
            cutV = verticalCut[v] if v in range(len(verticalCut)) else float('-inf')
            if cutH > cutV:
                cost += horizontalCut[h] * (v+1)
                h += 1
            else:
                cost += verticalCut[v] * (h+1)
                v += 1
        return cost
        
        
        