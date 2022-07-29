class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        numRows = len(heights)
        numCols = len(heights[0])
        
        canReachAtlantic = set()
        canReachPacific = set()
        
        answer = []
        
        def canReachOcean(r,c,reachesOcean, prevCell):
            if (r < 0 or c < 0 or
                r >= numRows or
                c >= numCols or
                (r,c) in reachesOcean or
                prevCell > heights[r][c]
            ):
                return
            reachesOcean.add((r,c))
            
            canReachOcean(r + 1,c,reachesOcean, heights[r][c])
            canReachOcean(r - 1,c,reachesOcean, heights[r][c])
            canReachOcean(r,c + 1,reachesOcean, heights[r][c])
            canReachOcean(r,c - 1,reachesOcean, heights[r][c])
        
        for r in range(numRows):
            for c in range(numCols):
                if not r or not c:
                    canReachOcean(r,c, canReachPacific, heights[r][c])
                if r == numRows - 1 or c == numCols - 1:
                    canReachOcean(r,c, canReachAtlantic, heights[r][c])
                    
        for r in range(numRows):
            for c in range(numCols):
                if (r,c) in canReachAtlantic and (r,c) in canReachPacific:
                    answer.append([r,c])
                    
        return answer
                    
    

        
            