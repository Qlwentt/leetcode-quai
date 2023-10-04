class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxArea = float('-inf')
        def dfs(row,col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] == 0 or
                (row,col) in visited):
                return 0
            visited.add((row,col))
            
            up = dfs(row-1,col)
            down = dfs(row+1,col)
            left = dfs(row, col-1)
            right = dfs(row, col+1)
            return up + down+ left+ right + 1
        
        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r,c)
                maxArea = max(area, maxArea)
        return maxArea
            