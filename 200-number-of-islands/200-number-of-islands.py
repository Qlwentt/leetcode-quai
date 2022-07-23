class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        numRows = len(grid)
        numCols = len(grid[0])
        
        numIslands = 0
        
        def dfs(r,c):
            if ( r < 0 or c < 0 or
                 r >= numRows or c >= numCols or
                 grid[r][c] == '0' or
                (r,c) in visited
            ):
                return False
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True
            
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == "1":
                    if dfs(row,col):
                        numIslands += 1
        
        return numIslands
            
            