class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        rows_highest = {}
        cols_highest = {}
        
        for r in range(ROWS):
            highest = float('-inf')
            for c in range(COLS):
                highest = max(grid[r][c], highest)
            rows_highest[r] = highest
        
        for c in range(COLS):
            highest = float('-inf')
            for r in range(ROWS):
                highest = max(grid[r][c], highest)
            cols_highest[c] = highest
        
        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                bound = min(rows_highest[r], cols_highest[c])
                answer += max(bound-grid[r][c], 0)
        return answer
                