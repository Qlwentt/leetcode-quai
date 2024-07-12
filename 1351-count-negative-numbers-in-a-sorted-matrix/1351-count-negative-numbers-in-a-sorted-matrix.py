class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] < 0:
                    count += 1
                    
        return count