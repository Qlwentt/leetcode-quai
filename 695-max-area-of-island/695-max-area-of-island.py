class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        visited = set ()
        def dfs(r,c, area):
            if (r < 0 or c < 0 or
                r >= numRows or c >= numCols or
                grid[r][c] == 0 or
                (r,c) in visited
            ):
                return area
            
            visited.add((r,c))
            area += 1
            
            area = dfs(r + 1,c, area)
            area = dfs(r - 1,c, area)
            area = dfs(r,c + 1, area)
            area = dfs(r,c - 1, area)
            
            return area
        
        maxArea = 0
        for row in range(numRows):
            for col in range(numCols):
                area = dfs(row, col, 0)
                maxArea = max(area, maxArea)
        return maxArea