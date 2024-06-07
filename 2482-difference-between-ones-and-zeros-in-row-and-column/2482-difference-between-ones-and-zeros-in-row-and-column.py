class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        answer = [[0]*COLS for _ in range(ROWS)]
        
        ones_rows = collections.defaultdict(int)
        ones_cols = collections.defaultdict(int)
        
        for r in range(ROWS):
            for c in range(COLS):
                ones_rows[r] += grid[r][c]
                ones_cols[c] += grid[r][c]
        
        for r in range(ROWS):
            for c in range(COLS):
                answer[r][c] = ones_rows[r] + ones_cols[c] - (ROWS-ones_rows[r]) - (COLS-ones_cols[c])
        
        return answer