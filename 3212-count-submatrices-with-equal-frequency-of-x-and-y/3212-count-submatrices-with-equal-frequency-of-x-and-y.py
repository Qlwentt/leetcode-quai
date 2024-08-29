class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        prefix_x = collections.defaultdict(lambda: collections.defaultdict(int))
        prefix_y = collections.defaultdict(lambda: collections.defaultdict(int))
        
        for r in range(ROWS):
            prefix_row_x = 0
            prefix_row_y = 0
            for c in range(COLS):
                prefix_row_x += 1 if grid[r][c] == "X" else 0
                prefix_row_y += 1 if grid[r][c] == "Y" else 0
                
                above_x = prefix_x[r-1][c]
                above_y = prefix_y[r-1][c]
                
                prefix_x[r][c] = above_x + prefix_row_x
                prefix_y[r][c] = above_y + prefix_row_y
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if prefix_x[r][c] == prefix_y[r][c] and prefix_x[r][c] > 0:
                    count += 1
        return count
    
# Time: O(N^2)
# Space: O(N^2)
                
        
        