class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        
        visited = set() # (r,c)
        
        def isNewIsland(r,c):
            if (r < 0 or c < 0 or
                r >= numRows or
                c >= numCols or
                grid[r][c] == "0" or
                (r,c) in visited
            ):
                return False
            
            visited.add((r,c))
            
            isNewIsland(r + 1,c)
            isNewIsland(r - 1 ,c)
            isNewIsland(r,c + 1)
            isNewIsland(r,c - 1)
            
            return True
        
        numIslands = 0
        
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1":
                    if isNewIsland(r,c):
                        numIslands += 1
        return numIslands
            