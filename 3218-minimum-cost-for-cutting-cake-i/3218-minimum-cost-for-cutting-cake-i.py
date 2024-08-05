class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        @cache
        def backtrack(h,v):
            if h == len(horizontalCut) and v == len(verticalCut):
                return 0
            
            if h in range(len(horizontalCut)):
                horiCut =  horizontalCut[h] * (v+1) + backtrack(h+1,v)
            else:
                horiCut = float('inf')
            if v in range(len(verticalCut)):
                vertCut = verticalCut[v] * (h+1) + backtrack(h,v+1) 
            else:
                vertCut = float('inf')
            return min(horiCut, vertCut)
        
        return backtrack(0,0)
                    
            
        