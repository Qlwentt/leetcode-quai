class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        cellsWaterFlows = []
        
        numRows = len(heights)
        numCols = len(heights[0])
        
        reachesPacific = set()
        reachesAtlantic = set()
        
        def canReachOcean(r,c, prevCell, reachesOcean):
            if (r < 0 or c < 0 or
                r >= numRows or c >= numCols or
                heights[r][c] < prevCell or
                (r,c) in reachesOcean
            ):
                return
            
        
            reachesOcean.add((r,c))
            
            canReachOcean(r + 1, c, heights[r][c], reachesOcean)
            canReachOcean(r - 1, c, heights[r][c], reachesOcean)
            canReachOcean(r, c + 1, heights[r][c], reachesOcean)
            canReachOcean(r, c - 1, heights[r][c], reachesOcean)
           
                
                
        
        for row in range(numRows):
            for col in range(numCols):
                if not row or not col:
                    canReachOcean(row,col, float("-inf"), reachesPacific)
                if row == numRows - 1 or col == numCols -1:
                    canReachOcean(row,col, float("-inf"), reachesAtlantic)
                    
        for r in range(numRows):
            for c in range(numCols):
                if (r,c) in reachesPacific and (r,c) in reachesAtlantic:
                    cellsWaterFlows.append([r,c])
    
        return cellsWaterFlows
            
            