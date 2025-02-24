class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def dfs(r,c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visited or
                grid[r][c] == 0):
                return 0
            
            visited.add((r,c))
            
            up = dfs(r-1, c)
            down = dfs(r+1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            
            return up + down + left + right + 1
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r,c)    
                    max_area = max(area, max_area)
                    
        return max_area
    
# Time: O (M*N)
# Space: O(M*N)